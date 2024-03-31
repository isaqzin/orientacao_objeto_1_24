number= int(input("digite um numero entre 0 e 10"))
control = 1

while True: 

    if number>=0 and number<=10:
        print(f"seu numero é {number}")
        break
    else:
       number= int(input("numero invalido digite um numero entre 0 e 10"))

print("fim do loop")