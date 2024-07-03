from package.maths.terms import TrianguloEquilatero
from package.maths.terms import Point

ponto1 = Point(0,0)
ponto2 = Point(0,6)
ponto3 = Point(3,5)

triangulo = TrianguloEquilatero(ponto1,ponto2,ponto3)

print(f' a area é {triangulo.area()}, a altura é {triangulo.altura()}, o baricentro é {triangulo.baricentro()} e o perimetro é {triangulo.perimetro()}')

triangulo.model()