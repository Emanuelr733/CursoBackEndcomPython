usuario = {}
nome=str(input("Digite o seu nome:"))
email=str(input("Digite o seu email:"))
idade=int(input("Digite a sua idade:"))
usuario["nome"] = nome
usuario["email"] = email
usuario["idade"] = idade
if usuario["idade"] >= 18:
    print(f"Bem-vindo, {usuario["nome"]}! Seu cadastro com o email {usuario["email"]} foi concluido.")
else:
    print("Acesso negado para menores.")