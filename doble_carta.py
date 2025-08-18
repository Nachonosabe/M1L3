def double_letter(str):
    result = ''
    for letter in str:
        result += letter * 2
    return result
def calcular(expr: str):
    """
    Calculadora básica que evalúa expresiones de suma, resta,
    multiplicación y división.
    Ejemplos: "2+2", "10-3", "5*4", "20/5"
    """
    try:

        permitido = "0123456789+-*/. "
        if not all(c in permitido for c in expr):
            return "❌ Solo puedes usar números y + - * /"

        resultado = eval(expr)
        return f"✅ Resultado: {resultado}"
    except ZeroDivisionError:
        return "❌ No se puede dividir entre cero"
    except Exception:
        return "❌ Operación inválida"
