from flask import Flask, request, jsonify, Response
import anthropic
import base64
import os
from config import TEMAS, PROMPT_BASE, PROMPT_CALCULADORA
 
app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
 
sesiones = {}
ultima_foto_bytes = None
 
 
def analizar_imagenes(fotos_b64, tema_key=None):
    if tema_key and tema_key in TEMAS:
        tema = TEMAS[tema_key]
        prompt = f"{PROMPT_CALCULADORA}\n\nTema: {tema['nombre']}\n\n{tema['ejemplo']}\n\nTenes 3 fotos de la misma imagen tomadas en distintos momentos. Usa la mas nitida para responder."
    else:
        prompt = f"{PROMPT_CALCULADORA}\n\nTenes 3 fotos de la misma imagen. Usa la mas nitida y describe lo que ves."
 
    content = []
    for b64 in fotos_b64:
        content.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": b64,
            }
        })
    content.append({"type": "text", "text": prompt})
 
    mensaje = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=600,
        messages=[{"role": "user", "content": content}]
    )
    return mensaje.content[0].text
 
 
@app.route("/foto", methods=["POST"])
def recibir_foto():
    global ultima_foto_bytes
 
    content_type = request.headers.get("Content-Type", "")
 
    # Modo 3 fotos (JSON con base64)
    if "application/json" in content_type:
        body = request.get_json()
        if not body:
            return jsonify({"error": "Sin datos"}), 400
 
        tema_key = body.get("tema", None)
        foto1 = body.get("foto1")
        foto2 = body.get("foto2")
        foto3 = body.get("foto3")
 
        if not foto1 or not foto2 or not foto3:
            return jsonify({"error": "Faltan fotos"}), 400
 
        # guardar ultima foto para ver en browser
        ultima_foto_bytes = base64.b64decode(foto3)
 
        try:
            resultado = analizar_imagenes([foto1, foto2, foto3], tema_key)
            sesiones["esp32"] = {"ultimo_resultado": resultado}
            return jsonify({"texto": resultado}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
 
    # Modo foto simple (jpeg directo)
    else:
        if not request.data:
            return jsonify({"error": "Sin datos"}), 400
 
        ultima_foto_bytes = request.data
        tema_key = request.headers.get("X-Tema", None)
        imagen_b64 = base64.standard_b64encode(request.data).decode("utf-8")
 
        try:
            resultado = analizar_imagenes([imagen_b64], tema_key)
            sesiones["esp32"] = {"ultimo_resultado": resultado}
            return jsonify({"texto": resultado}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
 
 
@app.route("/ultima-foto")
def ver_ultima_foto():
    if ultima_foto_bytes is None:
        return "No hay fotos recibidas aun.", 404
    return Response(ultima_foto_bytes, mimetype="image/jpeg")
 
 
@app.route("/ultimo-resultado")
def ver_ultimo_resultado():
    if "esp32" not in sesiones:
        return "Sin resultados aun.", 404
    return sesiones["esp32"]["ultimo_resultado"], 200
 
 
@app.route("/temas", methods=["GET"])
def listar_temas():
    return jsonify({k: v["nombre"] for k, v in TEMAS.items()}), 200
 
 
@app.route("/")
def index():
    foto_link = '<a href="/ultima-foto">Ver ultima foto</a>' if ultima_foto_bytes else "Sin fotos aun"
    resultado_link = '<a href="/ultimo-resultado">Ver ultimo resultado</a>' if "esp32" in sesiones else "Sin resultados aun"
    return f"""
    <h2>Servidor activo</h2>
    <p>{foto_link}</p>
    <p>{resultado_link}</p>
    """
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
