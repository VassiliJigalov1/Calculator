from flask import Flask, request, jsonify, Response
import anthropic
import base64
import os
from config import TEMAS, PROMPT_BASE

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Memoria temporal por sesión
sesiones = {}
ultima_foto_bytes = None  # guarda la ultima foto recibida

def dividir_en_bloques(texto, tam=130):
    return [texto[i:i+tam] for i in range(0, len(texto), tam)]

def analizar_imagen(imagen_bytes, tema_key=None):
    imagen_b64 = base64.standard_b64encode(imagen_bytes).decode("utf-8")

    if tema_key and tema_key in TEMAS:
        tema = TEMAS[tema_key]
        prompt = f"{PROMPT_BASE}\n\nTema solicitado: {tema['nombre']}\n\nEjemplo de referencia:\n{tema['ejemplo']}\n\nAhora analizá la imagen y respondé en base a ese tema."
    else:
        prompt = f"{PROMPT_BASE}\n\nAnalizá la imagen y describí lo que ves de forma clara y concisa."

    mensaje = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": imagen_b64,
                    },
                },
                {
                    "type": "text",
                    "text": prompt
                }
            ],
        }]
    )
    return mensaje.content[0].text


@app.route("/foto", methods=["POST"])
def recibir_foto():
    global ultima_foto_bytes

    if not request.data:
        return jsonify({"error": "Sin datos"}), 400

    # Guardar la foto para verla despues
    ultima_foto_bytes = request.data

    tema_key = request.headers.get("X-Tema", None)

    try:
        resultado = analizar_imagen(request.data, tema_key)
        bloques = dividir_en_bloques(resultado)

        sesiones["esp32"] = {
            "bloques": bloques,
            "total": len(bloques),
            "ultimo_resultado": resultado
        }

        return jsonify({
            "bloque": 0,
            "total": len(bloques),
            "texto": resultado  # mandamos todo el texto, no solo el primer bloque
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/ultima-foto")
def ver_ultima_foto():
    """Mostra la ultima foto recibida del ESP32 en el browser"""
    if ultima_foto_bytes is None:
        return "No hay fotos recibidas aun.", 404
    return Response(ultima_foto_bytes, mimetype="image/jpeg")


@app.route("/ultimo-resultado")
def ver_ultimo_resultado():
    """Muestra el ultimo texto que devolvio Claude"""
    if "esp32" not in sesiones:
        return "Sin resultados aun.", 404
    return sesiones["esp32"]["ultimo_resultado"], 200


@app.route("/bloque/<int:numero>", methods=["GET"])
def obtener_bloque(numero):
    if "esp32" not in sesiones:
        return jsonify({"error": "Sin sesion activa"}), 404

    datos = sesiones["esp32"]

    if numero < 0 or numero >= datos["total"]:
        return jsonify({"error": "Fuera de rango"}), 400

    return jsonify({
        "bloque": numero,
        "total": datos["total"],
        "texto": datos["bloques"][numero]
    }), 200


@app.route("/temas", methods=["GET"])
def listar_temas():
    return jsonify({k: v["nombre"] for k, v in TEMAS.items()}), 200


@app.route("/")
def index():
    fotos = sesiones.get("esp32", {})
    total = fotos.get("total", 0)
    foto_link = '<a href="/ultima-foto">Ver ultima foto</a>' if ultima_foto_bytes else "Sin fotos aun"
    resultado_link = '<a href="/ultimo-resultado">Ver ultimo resultado</a>' if total > 0 else "Sin resultados aun"
    return f"""
    <h2>Servidor activo</h2>
    <p>{foto_link}</p>
    <p>{resultado_link}</p>
    <p>Bloques en memoria: {total}</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
