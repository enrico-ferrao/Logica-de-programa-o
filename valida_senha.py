def se(tentativa = 1):
    password = "1234"
    tokey_key = input("Qual a senha: ")

    if tentativa >= 3:
        print("Converse com administrador...")

    if tokey_key != password:
        print("Senha incorreta!")
        return se(tentativa + 1)
    else:
        print("Senha correta, ativação de sistema iniciando.....")

se()