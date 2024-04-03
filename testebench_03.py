from package.maths.terms import point

ponto = point(3,4)

print(f'a distancia do ponto à origem é {ponto.distanceFC()}')

print (f'o angulo em relação a reta que passa pela origem e pelo ponto em relação ao x é {ponto.anguloX()} rad e em graus é {ponto.anguloX()*180/3,14}')