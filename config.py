PROMPT_CALCULADORA = """
El resultado sera mandado a un calculadora ti-84, asique sigue las reglas de formato:
 
REGLAS DE FORMATO:
- Escribe en lineas, cada linea tiene MAXIMO 16 caracteres contando espacios.
- NO uses tildes ni acentos: escribi "a" no "a con tilde", "u" no "u con tilde".
- NO uses caracteres especiales: solo letras sin acento, numeros y: + - * / = ( ) [ ] ^ . , _
- En vez de x (multiplicacion) usa: *, en vez de simbolo sigma usa: sigma, en vez de % usa pct.
- Usa 2 decimales como maximo.
- Usa abreviaciones: E[X], Var, PP, Ptarifa, Ded, sin, tend, fact, etc.
- NO uses palabras largas en lo posible.
- no expliques el procedimiendo
- No hagas espacio entre lineas ni uases separadores entre lineas
"""
 
TEMAS = {
    "1": {
        "nombre": "Sigue la resolucion del ejercicio",
        "ejemplo": ""
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
        "ejemplo": ""
    }
}
