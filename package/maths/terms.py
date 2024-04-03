import math

class Reta():


    def __init__(self,a,b):

        self.a = a
        self.b = b


    def interpolar(self,x):

        y = self.a * x + self.b
        return y

    
    def model(self):

        print(f'Os parâmertros do meu modelo de reta são: a={self.a}, b={self.b}')


class Circle():

    def __init__(self,raio,a,b):

        self.raio=raio
        self.a=a
        self.b=b

    def area(self):

        area= 3.14*self.raio**2
        return area

    def equation(self):

        print(f'{self.raio}²= (y-{self.b})² + (x-{self.a})²')

    def perimetro(self):

        perimetro=2*3.14*self.raio
        return perimetro
    
class point():


    def __init__(self,x,y):

        self.x=x
        self.y=y

    def distanceFC(self):

        distanceFC = math.sqrt(self.x**2 + self.y**2)
        return distanceFC
    
    def anguloX(self):

        anguloX = math.atan(self.y/self.x)

        return anguloX

    
