nome=input("digite seu nome:\n")

while True:
    if len(nome)<3:
        print("digite um nome com mais  de 3 caracteres\n")
        nome=input("digite seu nome:\n")
    else:
        break

idade = int(input("Digite sua idade:\n"))

while True:
    if idade<0 or idade>150:
        print("idade invalida:\n")
        idade = int(input("Digite sua idade:\n"))
    else:
        break

salario = float(input("digite quanto vc recebe:\n"))

while True:
    if salario<=0:
        print("salario invalido\n")
        salario = float(input("digite quanto vc recebe:\n"))
    else:
        break

sexo = input("digite F se é femea e M se é macho\n")

while True:
    if sexo == 'F' or sexo == 'M':
        break
    else:
        print("sexo invalido\n")
        sexo = input("digite F se é femea e M se é macho\n")

estado_civil= input("digite C se é casado, S solteiro, V viuvo, D divorciado\n")

while True:
    if estado_civil =='C' or estado_civil =='S' or estado_civil =='V' or estado_civil =='D' :
        break
    else:
         print("estado civil invalido")
         estado_civil= input("digite C se é casado, S solteiro, V viuvo, D divorciado\n") 

print(f"seu nome é {nome}\nsua idade é {idade}\nseu salario é {salario}\nseu sexo é {sexo}\nseu estado civil é {estado_civil} ")