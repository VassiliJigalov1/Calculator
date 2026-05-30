from flask import Flask, request, jsonify
import anthropic
import base64
import os
from config import TEMAS, PROMPT_BASE

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Memoria temporal por sesión
sesiones = {}

def dividir_en_bloques(texto, tam=130):
    """Divide el texto en bloques de 'tam' caracteres"""
    return [texto[i:i+tam] for i in range(0, len(texto), tam)]

def analizar_imagen(imagen_bytes, tema_key=None):
    """Envía imagen + prompt a Claude y retorna la respuesta"""
    imagen_b64 = base64.standard_b64encode(imagen_bytes).decode("utf-8")

    # Construir prompt según si se eligió tema o no
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
    """
    Recibe la foto del ESP32.
    Parámetro opcional en header: X-Tema (1-5)
    """
    if not request.data:
        return jsonify({"error": "Sin datos"}), 400

    # Leer tema si fue enviado (header X-Tema: 1, 2, 3, 4 o 5)
    tema_key = request.headers.get("X-Tema", None)

    try:
        resultado = analizar_imagen(request.data, tema_key)
        bloques = dividir_en_bloques(resultado)

        sesiones["esp32"] = {
            "bloques": bloques,
            "total": len(bloques)
        }

        return jsonify({
            "bloque": 0,
            "total": len(bloques),
            "texto": bloques[0]
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/bloque/<int:numero>", methods=["GET"])
def obtener_bloque(numero):
    """Retorna un bloque específico de la última respuesta"""
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
    """Endpoint de diagnóstico: muestra los temas configurados"""
    return jsonify({k: v["nombre"] for k, v in TEMAS.items()}), 200


@app.route("/")
def index():
    fotos = sesiones.get("esp32", {})
    total = fotos.get("total", 0)
    return f"Servidor activo. Bloques en memoria: {total}. Temas: {list(TEMAS.keys())}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
