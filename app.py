from flask import Flask, request, jsonify, Response
import anthropic
import base64
import re
import os
from config import TEMAS, PROMPT_CALCULADORA

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY")

sesiones = {}
ultima_foto_bytes = None


def detectar_media_type(foto_bytes):
    """Detecta el media_type real de la imagen a partir de sus 'magic bytes'."""
    if foto_bytes[:2] == b'\xff\xd8':
        return "image/jpeg"
    elif foto_bytes[:8] == b'\x89PNG\r\n\x1a\n':
        return "image/png"
    elif foto_bytes[:6] in (b'GIF87a', b'GIF89a'):
        return "image/gif"
    elif foto_bytes[:4] == b'RIFF' and foto_bytes[8:12] == b'WEBP':
        return "image/webp"
    else:
        return "image/jpeg"  # fallback


def parsear_paginas(texto):
    """Extrae el contenido de cada bloque ```...``` y devuelve una lista de strings."""
    patron = r'```([\s\S]*?)```'
    paginas = re.findall(patron, texto)
    return [p.strip() for p in paginas if p.strip()]


def analizar_imagenes(fotos_bytes, tema_key=None):
    if tema_key and tema_key in TEMAS:
        tema = TEMAS[tema_key]
        ejemplo = tema.get('ejemplo', '')
        prompt = f"{PROMPT_CALCULADORA}\n\nTema: {tema['nombre']}\n\n{ejemplo}"
    else:
        prompt = f"{PROMPT_CALCULADORA}"

    content = []
    for foto in fotos_bytes:
        b64 = base64.standard_b64encode(foto).decode("utf-8")
        media_type = detectar_media_type(foto)
        content.append({
            "type": "image",
            "source": {"type": "base64", "media_type": media_type, "data": b64}
        })
    content.append({"type": "text", "text": prompt})

    mensaje = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=16000,
        messages=[{"role": "user", "content": content}]
    )

    # Concatena todos los bloques de tipo "text" de la respuesta
    textos = [block.text for block in mensaje.content if block.type == "text"]
    return "\n".join(textos)


@app.route("/foto", methods=["POST"])
def recibir_foto():
    global ultima_foto_bytes

    content_type = request.headers.get("Content-Type", "")

    if "multipart/form-data" in content_type:
        foto1 = request.files.get("foto1")
        foto2 = request.files.get("foto2")
        foto3 = request.files.get("foto3")

        if not foto1 or not foto2 or not foto3:
            return jsonify({"error": "Faltan fotos"}), 400

        bytes1 = foto1.read()
        bytes2 = foto2.read()
        bytes3 = foto3.read()
        ultima_foto_bytes = bytes3
        tema_key = request.headers.get("X-Tema", None)

        try:
            resultado_raw = analizar_imagenes([bytes1, bytes2, bytes3], tema_key)
            paginas = parsear_paginas(resultado_raw)
            sesiones["esp32"] = {
                "ultimo_resultado": resultado_raw,
                "paginas": paginas
            }
            return jsonify({
                "texto": resultado_raw,
                "paginas": paginas,
                "total_paginas": len(paginas)
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        if not request.data:
            return jsonify({"error": "Sin datos"}), 400

        ultima_foto_bytes = request.data
        tema_key = request.headers.get("X-Tema", None)

        try:
            resultado_raw = analizar_imagenes([request.data], tema_key)
            paginas = parsear_paginas(resultado_raw)
            sesiones["esp32"] = {
                "ultimo_resultado": resultado_raw,
                "paginas": paginas
            }
            return jsonify({
                "texto": resultado_raw,
                "paginas": paginas,
                "total_paginas": len(paginas)
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.route("/ultima-foto")
def ver_ultima_foto():
    if ultima_foto_bytes is None:
        return "No hay fotos recibidas aun.", 404
    media_type = detectar_media_type(ultima_foto_bytes)
    return Response(ultima_foto_bytes, mimetype=media_type)


@app.route("/ultimo-resultado")
def ver_ultimo_resultado():
    if "esp32" not in sesiones:
        return "Sin resultados aun.", 404
    return sesiones["esp32"]["ultimo_resultado"], 200


@app.route("/paginas")
def ver_paginas():
    """Devuelve las paginas parseadas como JSON."""
    if "esp32" not in sesiones:
        return jsonify({"error": "Sin resultados aun."}), 404
    paginas = sesiones["esp32"].get("paginas", [])
    return jsonify({
        "paginas": paginas,
        "total_paginas": len(paginas)
    }), 200


@app.route("/paginas/<int:numero>")
def ver_pagina(numero):
    """Devuelve una pagina especifica (base 1)."""
    if "esp32" not in sesiones:
        return jsonify({"error": "Sin resultados aun."}), 404
    paginas = sesiones["esp32"].get("paginas", [])
    if numero < 1 or numero > len(paginas):
        return jsonify({
            "error": f"Pagina {numero} no existe. Total: {len(paginas)}"
        }), 404
    return jsonify({
        "pagina": numero,
        "total_paginas": len(paginas),
        "contenido": paginas[numero - 1]
    }), 200


@app.route("/temas")
def listar_temas():
    return jsonify({k: v["nombre"] for k, v in TEMAS.items()}), 200


@app.route("/")
def index():
    foto_link = '<a href="/ultima-foto">Ver ultima foto</a>' if ultima_foto_bytes else "Sin fotos aun"
    resultado_link = '<a href="/ultimo-resultado">Ver ultimo resultado</a>' if "esp32" in sesiones else "Sin resultados aun"
    paginas_link = '<a href="/paginas">Ver paginas JSON</a>' if "esp32" in sesiones else ""
    return (
        f"<h2>Servidor activo</h2>"
        f"<p>{foto_link}</p>"
        f"<p>{resultado_link}</p>"
        f"<p>{paginas_link}</p>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
