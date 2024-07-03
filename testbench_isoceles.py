from package.maths.terms import TrianguloIsoceles
from package.maths.terms import Point

ponto1 = Point(4,2)
ponto2 = Point(6,7)
ponto3 = Point(8,2)

triangulo = TrianguloIsoceles(ponto1,ponto2,ponto3)

print(f' a area é {triangulo.area()}, a altura é {triangulo.altura()}, o baricentro é {triangulo.baricentro()} e o perimetro é {triangulo.perimetro()}')

triangulo.model()