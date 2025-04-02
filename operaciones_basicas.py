"""Módulo que contiene clases para operaciones matemáticas básicas y cálculo de promedio."""


class OperacionesBasicas:
    """Clase que realiza operaciones básicas como suma y resta."""

    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Devuelve el resultado almacenado."""
        return self.resultado


class CalculadoraPromedio:
    """Clase que trabaja con listas numéricas."""

    def __init__(self, valores):
        """Inicializa con una lista de valores."""
        self.valores = valores

    def calcular_promedio(self):
        """Calcula el promedio de los valores."""
        return sum(self.valores) / len(self.valores)

    def agregar_valor(self, valor):
        """Añade un nuevo valor a la lista."""
        self.valores.append(valor)


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

if __name__ == "__main__":
    # Operaciones básicas
    ops = OperacionesBasicas()
    ops.sumar(NUM1, NUM2)
    print(f"Suma: {ops.obtener_resultado()}")

    ops.restar(NUM1, NUM2)
    print(f"Resta: {ops.obtener_resultado()}")

    # Cálculo de promedio
    calc = CalculadoraPromedio(NUMEROS)
    print(f"Promedio inicial: {calc.calcular_promedio()}")

    calc.agregar_valor(6)
    print(f"Promedio con nuevo valor: {calc.calcular_promedio()}")
