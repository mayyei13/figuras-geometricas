"""Este módulo define clases para figuras geométricas y métodos para calcular sus áreas."""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""

    @abstractmethod
    def obtener_nombre(self):
        """Método abstracto para obtener el nombre de la figura."""

class Rectangulo(FiguraGeometrica):
    """Clase para representar un rectángulo y calcular su área."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        area = self.base * self.altura
        return area

    def obtener_nombre(self):
        """Devuelve el nombre de la figura."""
        return "Rectángulo"

    def obtener_perimetro(self):
        """Calcula el perímetro del rectángulo."""
        perimetro = 2 * (self.base + self.altura)
        return perimetro


class Triangulo(FiguraGeometrica):
    """Clase para representar un triángulo y calcular su área."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        area = (self.base * self.altura) / 2
        return area

    def obtener_nombre(self):
        """Devuelve el nombre de la figura."""
        return "Triángulo"

    def obtener_perimetro(self, lado1, lado2):
        """Calcula el perímetro del triángulo dado tres lados."""
        perimetro = self.base + lado1 + lado2
        return perimetro


class Circulo(FiguraGeometrica):
    """Clase para representar un círculo y calcular su área."""

    def __init__(self, radio):
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        area = self.pi * (self.radio ** 2)
        return area

    def obtener_nombre(self):
        """Devuelve el nombre de la figura."""
        return "Círculo"

    def obtener_perimetro(self):
        """Calcula el perímetro del círculo (circunferencia)."""
        perimetro = 2 * self.pi * self.radio
        return perimetro


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas y perímetros
    print(f"El área del {rectangulo.obtener_nombre()} es: {rectangulo.calcular_area()}")
    print(f"El perímetro del {rectangulo.obtener_nombre()} es: {rectangulo.obtener_perimetro()}")
    print(f"El área del {triangulo.obtener_nombre()} es: {triangulo.calcular_area()}")
    print(
        f"El perímetro del {triangulo.obtener_nombre()} es: {triangulo.obtener_perimetro(5, 6)}")
    print(f"El área del {circulo.obtener_nombre()} es: {circulo.calcular_area()}")
    print(f"El perímetro del {circulo.obtener_nombre()} es: {circulo.obtener_perimetro()}")
