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
        "nombre": "Resuelve el ejercicio con menor numero",
        "ejemplo": (
            "si ves dos ejercicios y uno dice ejercicio 2 y otro ejercicio 4 resluelve el 2"
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
