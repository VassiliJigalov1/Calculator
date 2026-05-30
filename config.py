# ============================================================
#  CONFIGURACIÓN DE TEMAS — EDITÁ SOLO ESTE ARCHIVO
#  Cada tecla (1-5) del ESP32 corresponde a una clave aquí.
#  Cambiá "nombre" y "ejemplo" sin tocar nada más.
# ============================================================

# Prompt base que siempre se envía a la IA
# Podés modificarlo para cambiar el tono o el idioma de respuesta
PROMPT_BASE = (
    "Sos un asistente especializado en cálculos actuariales. "
    "Respondé siempre en español, de forma clara y concisa. "
    "Si hay ejercicios o fórmulas en la imagen, resolvelos paso a paso."
)

# Temas asociados a las teclas 1-5
# "nombre": descripción corta del tema
# "ejemplo": ejemplo de ejercicio que guía a la IA sobre qué tipo de respuesta dar
TEMAS = {
    "1": {
        "nombre": "Interés compuesto y valor del dinero en el tiempo",
        "ejemplo": (
            "Ejemplo: Un capital de $10.000 se invierte al 8% anual durante 5 años. "
            "¿Cuál es el monto final con capitalización anual? "
            "Mostrá la fórmula M = C(1+i)^n y el resultado."
        )
    },
    "2": {
        "nombre": "Anualidades y rentas",
        "ejemplo": (
            "Ejemplo: Se depositan $500 al final de cada mes durante 3 años "
            "con una tasa del 6% anual convertible mensualmente. "
            "Calculá el valor futuro de la anualidad."
        )
    },
    "3": {
        "nombre": "Tablas de mortalidad y probabilidades de vida",
        "ejemplo": (
            "Ejemplo: Dado que la probabilidad de muerte entre 40 y 41 años es q_40=0.003, "
            "calculá la probabilidad de que una persona de 40 años sobreviva 2 años más."
        )
    },
    "4": {
        "nombre": "Seguros de vida y valores actuariales",
        "ejemplo": (
            "Ejemplo: Calculá el valor presente neto actuarial de un seguro de vida "
            "que paga $100.000 al fallecimiento, para una persona de 35 años, "
            "usando una tasa de interés del 5% y la tabla de mortalidad dada."
        )
    },
    "5": {
        "nombre": "Reservas matemáticas y primas",
        "ejemplo": (
            "Ejemplo: Calculá la prima nivelada anual para un seguro de vida entera "
            "emitido a una persona de 30 años, con suma asegurada de $50.000, "
            "tasa de interés 4% y tabla de mortalidad estándar."
        )
    },
}
