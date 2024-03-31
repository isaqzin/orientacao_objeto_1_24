usuario= input("digite seu usuario: \n")
senha = input("Digite sua senha: \n")


while True:


    if usuario == senha:
        print("A senha deve ser diferente do usuario")
        senha = input("Digite outra senha: \n")
    else:
        break

print(f"seu usuario é {usuario}")
print(f"sua senha é {senha}")