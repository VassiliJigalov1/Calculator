PROMPT_CALCULADORA = """

REGLAS DE FORMATO:
- Escribe en lineas, cada linea tiene MAXIMO 16 caracteres contando espacios.
- NO uses tildes ni acentos: escribi "a" no "a con tilde", "u" no "u con tilde".
- NO uses caracteres especiales: solo letras sin acento, numeros y: + - * / = ( ) [ ] ^ . , _
- En vez de x (multiplicacion) usa: *, en vez de simbolo sigma usa: sigma, en vez de % usa pct.
- Usa 2 decimales como maximo.
- Usa abreviaciones: E[X], Var, PP, Ptarifa, Ded, sin, tend, fact, etc.
- NO uses palabras largas en lo posible.
- no expliques el procedimiendo, excepto en "Sigue la resolucion del ejercicio con explicaciones breves" , "Tema libre con explicacion breve", "Teorico"
- No hagas espacio entre lineas ni uases separadores entre lineas
"""
 
TEMAS = {
    "1": {
        "nombre": "Sigue la resolucion del ejercicio",
        "ejemplo": ""
    },
    "2": {
        "nombre": "Sigue la resolucion del ejercicio con explicaciones breves",
        "ejemplo": ""
    },
    "3": {
        "nombre": "Tablas de mortalidad y probabilidades de vida",
        "ejemplo": (
            "Ejemplo: Dado que la probabilidad de muerte entre 40 y 41 anos es q_40=0.003, "
            "calcula la probabilidad de que una persona de 40 anos sobreviva 2 anos mas."
        )
    },
    "4": {
        "nombre": "Teorico",
        "ejemplo": ""
    },
    "5": {
        "nombre": "Tema libre con explicacion breve",
        "ejemplo": ""
    },
    "6": {
        "nombre": "Tema libre",
        "ejemplo": ""
    }
}
