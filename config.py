from pathlib import Path
from functools import lru_cache

BASE_DIR = Path(__file__).parent
PROMPTS_DIR = BASE_DIR / "prompts"

@lru_cache(maxsize=None)
def _cargar(nombre: str) -> str:
    ruta = PROMPTS_DIR / f"{nombre}.txt"
    try:
        return ruta.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""

PROMPT_CALCULADORA = _cargar("calculadora")

TEMAS = {
    "1": {"nombre": "Sigue la resolucion",        "ejemplo": ""},
    "2": {"nombre": "ART Argentina",              "ejemplo": _cargar("art")},
    "3": {"nombre": "Tarificacion",               "ejemplo": _cargar("tarificacion")},
    "4": {"nombre": "Teorico",                    "ejemplo": _cargar("teorico")},
    "5": {"nombre": "Tema libre con explicacion", "ejemplo": ""},
    "6": {"nombre": "Resuelve",                   "ejemplo": ""},
}
