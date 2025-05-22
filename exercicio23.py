class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def obter_perimetro(self):
        return self.a + self.b + self.c

    def obter_tipo(self):
        if self.a == self.b == self.c:
            return "Equilátero"
        elif self.a == self.b or \
                self.b == self.c or \
                self.a == self.c:
            return "Isósceles"
        else:
            return "Escaleno"


triangulo = Triangulo(3, 4, 5)
print("Perímetro:", triangulo.obter_perimetro())
print("Tipo:", triangulo.obter_tipo())
