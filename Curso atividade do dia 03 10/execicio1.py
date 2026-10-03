def verificar_acesso(usuario, senha):
    usuario_correto = "admin"
    senha_correta = "1234"

    if usuario == usuario_correto and senha == senha_correta:
        return "Acesso permitido"
    elif usuario != usuario_correto and senha == senha_correta:
        return "Usuário incorreto"
    elif usuario == usuario_correto and senha != senha_correta:
        return "Senha incorreta"
    else:
        return "Usuário e senha incorretos"


usuario = input("Usuário: ")
senha = input("Senha: ")

print(verificar_acesso(usuario, senha))