# ============================================================
#  CONFIGURACIÓN DE TEMAS — EDITÁ SOLO ESTE ARCHIVO
# ============================================================
 
PROMPT_BASE = (
    "Sos un asistente especializado en cálculos actuariales. "
    "Respondé siempre en español, de forma clara y concisa. "
    "Si hay ejercicios o fórmulas en la imagen, resolvelos paso a paso."
)
 
PROMPT_CALCULADORA = (
    "Respondé en español, sin markdown, sin asteriscos, sin guiones, sin titulos. "
    "Texto plano solamente. Maximo 500 caracteres. "
    "Respondé de forma directa y concisa como si fuera para una pantalla muy pequeña."
)
 
TEMAS = {
    "1": {
        "nombre": "Interes compuesto y valor del dinero en el tiempo",
        "ejemplo": (
            "Ejemplo: Un capital de $10.000 se invierte al 8% anual durante 5 anos. "
            "Cual es el monto final con capitalizacion anual? "
            "Mostra la formula M = C(1+i)^n y el resultado."
        )
    },
    "2": {
        "nombre": "Anualidades y rentas",
        "ejemplo": (
            "Ejemplo: Se depositan $500 al final de cada mes durante 3 anos "
            "con una tasa del 6% anual convertible mensualmente. "
            "Calcula el valor futuro de la anualidad."
        )
    },
    "3": {
        "nombre": "Tablas de mortalidad y probabilidades de vida",
        "ejemplo": (
            "Ejemplo: Dado que la probabilidad de muerte entre 40 y 41 anos es q_40=0.003, "
            "calcula la probabilidad de que una persona de 40 anos sobreviva 2 anos mas."
        )
    },
    "4": {
        "nombre": "Seguros de vida y valores actuariales",
        "ejemplo": (
            "Ejemplo: Calcula el valor presente neto actuarial de un seguro de vida "
            "que paga $100.000 al fallecimiento, para una persona de 35 anos, "
            "usando una tasa de interes del 5% y la tabla de mortalidad dada."
        )
    },
    "5": {
        "nombre": "Reservas matematicas y primas",
        "ejemplo": (
            "Ejemplo: Calcula la prima nivelada anual para un seguro de vida entera "
            "emitido a una persona de 30 anos, con suma asegurada de $50.000, "
            "tasa de interes 4% y tabla de mortalidad estandar."
        )
    },
    "6": {
        "nombre": "Tema libre",
        "ejemplo": (
            "Analiza la imagen y describe detalladamente lo que ves. "
            "Si hay texto, transcribilo. Si hay formulas, identificalas."
        )
    },
}

