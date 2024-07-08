import math
from abc import ABC, abstractmethod

class Point():

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distanceFC(self):

        distanceFC = math.sqrt(self.x**2 + self.y**2)
        return distanceFC
    
    def distancePoints(self, point):
        x2 = point.x
        y2 = point.y
        distancePoints = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        return distancePoints  
     
    def anguloX(self):

        if self.x != 0:
            anguloX = math.atan(self.y/self.x)
        else:
            anguloX=0
            
        return anguloX

class SegReta():


    def __init__(self,point_origem, point_final):

        self.point_origem = point_origem
        self.point_final = point_final


    def tamanho(self):

        tamanho = math.sqrt((self.point_final.x - self.point_origem.x)**2 + (self.point_final.y - self.point_origem.y)**2)
        return tamanho

    
    def model(self):

        print(f'As coordenadas do segmento de reta são Origem=[{self.point_origem.x},{self.point_origem.y}] e Fim=[{self.point_final.x},{self.point_final.y}]')


class Circle():

    #centro é um ponto
    def __init__(self,centro,raio):

        self.raio=raio
        self.centro = centro

    def area(self):

        area= 3.14*self.raio**2
        return area

    def equation(self):

        print(f'{self.raio}²= (y-{self.centro.y})² + (x-{self.centro.x})²')

    def perimetro(self):

        perimetro=2*3.14*self.raio
        return perimetro

class Quadrado():
        
        def __init__(self,lado):

            self.lado = lado
            self.origem = Point(0,0) #composicao
            self.centro = Point(0,0)
            self.sup_dir = Point()
            self.sup_esq = Point()
            self.inf_dir = Point()
            self.inf_esq = Point()

        def _setPoints(self):

            self.sup_dir.y = self.origem.y + self.lado
            self.sup_dir.x = self.origem.x + self.lado
            self.sup_esq.x = self.origem.x
            self.sup_esq.y = self.origem.y + self.lado
            self.inf_dir.x = self.origem.x + self.lado
            self.inf_dir.y = self.origem.y 
            self.inf_esq = self.origem
 
        def setOrigem(self,ponto):

            self.origem= ponto

        def area(self):

            area= self.lado**2
            return area
    
        def perimetro(self):

            perimetro= 4*self.lado
            return perimetro

        def model(self):

         print(f' meu quadrado tem lado {self.lado} e tem origem em [{self.origem.x}, {self.origem.y}]')

        def diagonal(self):
            diagonal= math.sqrt(2*(self.lado**2))
            return diagonal
        
        def getCentro(self):
            diagonal= math.sqrt(2*(self.lado**2))
            self.centro.x= (diagonal/2) + self.origem.x
            self.centro.y= (diagonal/2) + self.origem.y
            return self.centro.x, self.centro.y
            


class Retangulo(Quadrado):

    #lado é a altura Y, lado 2 é o comprimento X    
    def __init__(self, lado, lado2):
        super().__init__(lado)
        self.lado2= lado2
        self.sup_dir = Point()
        self.sup_esq = Point()
        self.inf_dir = Point()
        self.inf_esq = Point()

    def _setPoints(self):

        self.sup_dir.y = self.origem.y + self.lado
        self.sup_dir.x = self.origem.x + self.lado2
        self.sup_esq.x = self.origem.x
        self.sup_esq.y = self.origem.y + self.lado
        self.inf_dir.x = self.origem.x + self.lado2
        self.inf_dir.y = self.origem.y 
        self.inf_esq = self.origem

    def area(self):

        area= self.lado * self.lado2
        return area
    
    def perimetro(self):

        perimetro= 2*self.lado + 2*self.lado2
        return perimetro
    
    def model(self):

        print(f' meu retangulo tem lados {self.lado} e {self.lado2} tem origem em [{self.origem.x}, {self.origem.y}]')

    def diagonal(self):
        diagonal = math.sqrt(self.lado**2 + self.lado2**2)
        return diagonal
    
    def getCentro(self):
        diagonal= math.sqrt(self.lado**2 + self.lado2**2)
        self.centro.x= (diagonal/2) + self.origem.x
        self.centro.y= (diagonal/2) + self.origem.y
        return self.centro.x, self.centro.y
    
#Eu sei que daria pra fazer todos os tipos de triangulo em uma só classe
#mas estudando vi a abstração e quis por, n tive muita ideia 
#se pareceu forçado, releve :) 
#ai vou mudar só a formula de calculo de area em cada triangulo ou algo que 
#achar de diferente em cada 
class Triangulo(ABC):

    def __init__(self, ponto1, ponto2,ponto3):

        self.ponto1=ponto1
        self.ponto2=ponto2
        self.ponto3=ponto3
        self.lado1= math.sqrt((ponto2.x - ponto1.x)**2 + (ponto2.y - ponto1.y)**2)
        self.lado2= math.sqrt((ponto2.x - ponto3.x)**2 + (ponto2.y - ponto3.y)**2)
        self.lado3= math.sqrt((ponto3.x - ponto1.x)**2 + (ponto3.y - ponto1.y)**2)

    def _verificarTriangulo(self):

        if (self.lado1 + self.lado2 )> self.lado3 and (self.lado3 + self.lado2 )> self.lado1 and (self.lado1 + self.lado3 )> self.lado2:
            return True
        else:
            return False
        

    def perimetro(self):

        tester = self._verificarTriangulo()
        if tester == True:
            perimetro= self.lado1 + self.lado2 + self.lado3
            return perimetro
        else:
             print("Seus pontos não formam um triangulo.")
    
    def baricentro(self):

        tester = self._verificarTriangulo()
        if tester == True:
            x= (self.ponto1.x + self.ponto2.x + self.ponto3.x)/3
            y =(self.ponto1.y + self.ponto2.y + self.ponto3.y)/3
            return x,y
        else:
             print("Seus pontos não formam um triangulo.")         
    
    @abstractmethod
    def area(self):
        pass
    def altura(self):
        pass
    def model(self):
        pass

class TrianguloEquilatero(Triangulo):

    def __init__(self, ponto1, ponto2, ponto3):
        super().__init__(ponto1, ponto2, ponto3)

    def area(self):
        tester = self._verificarTriangulo()
        if tester == True:
            area = ((self.lado1**2)*math.sqrt(3))/4
            return area
        else:
             print("Seus pontos não formam um triangulo.")   

    def altura(self):
        tester = self._verificarTriangulo()
        if tester == True:
            altura =(self.lado1*math.sqrt(3))/2
            return altura
        else:
             print("Seus pontos não formam um triangulo.")   
        
    def model(self):
        tester = self._verificarTriangulo()
        if tester == True:
            print(f'nosso triangulo tem coordenadas iguais a [{self.ponto1.x},{self.ponto1.y}],[{self.ponto2.x},{self.ponto2.y}],[{self.ponto3.x},{self.ponto3.y}] e lados iguais a {self.lado1}')
        else:
             print("Seus pontos não formam um triangulo.")   
class TrianguloIsoceles(Triangulo):

    def __init__(self, ponto1, ponto2, ponto3):
        super().__init__(ponto1, ponto2, ponto3)
        


    def altura(self):
        tester = self._verificarTriangulo()
        if tester == True:
            if self.lado1 == self.lado2:
                altura = (self.lado1**2 - (self.lado3**2)/4)**0.5
                return altura
            elif self.lado1 == self.lado3:
                altura = (self.lado1**2 - (self.lado2**2)/4)**0.5
                return altura
            elif self.lado2 == self.lado3:
                altura = (self.lado2**2 - (self.lado1**2)/4)**0.5
                return altura 
            else:
                print("suas opções são invalidas")
                altura=0.00
                return altura 
        else:
            print("Seus pontos não formam um triangulo.")   

    def area(self):
        tester = self._verificarTriangulo()
        if tester == True:
            h = self.altura()
        
            if self.lado1 == self.lado2:
                base= self.lado3
            elif self.lado1 == self.lado3:
                base=self.lado2
            elif self.lado2 == self.lado3:
                base= self.lado1
            else:
                print("suas opções são invalidas")
                base=0.00 

            area = (base*h)/2
            return area
        else:
           print("Seus pontos não formam um triangulo.")

    def model(self):
        tester = self._verificarTriangulo()
        if tester == True:
            print(f'nosso triangulo tem coordenadas iguais a [{self.ponto1.x},{self.ponto1.y}],[{self.ponto2.x},{self.ponto2.y}],[{self.ponto3.x},{self.ponto3.y}] e lados iguais a {self.lado1}, {self.lado2} e {self.lado3}') 
        else:
             print("Seus pontos não formam um triangulo.")   