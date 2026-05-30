# ============================================================
#  CONFIGURACIÓN DE TEMAS — EDITÁ SOLO ESTE ARCHIVO
#  Teclas 1-5: temas fijos de cálculo actuarial
#  Tecla 6:    tema libre — cambialo cuando quieras
# ============================================================

PROMPT_BASE = (
    "Sos un asistente especializado en cálculos actuariales. "
    "Respondé siempre en español, de forma clara y concisa. "
    "Si hay ejercicios o fórmulas en la imagen, resolvelos paso a paso."
)

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

    # ── Tema libre — cambiá esto cuando quieras ──────────────
    # No necesitás tocar el ESP32 ni la Casio, solo este bloque
    "6": {
        "nombre": "Tema libre",
        "ejemplo": (
            "Analizá la imagen y describí detalladamente lo que ves. "
            "Si hay texto, transcribilo. Si hay fórmulas, identificalas."
        )
    },
}

