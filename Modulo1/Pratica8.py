def calcular_media(n1,n2,n3):
    return (n1+n2+n3)/3
n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))
n3=float(input("Digite a terceira nota:"))
media = calcular_media(n1,n2,n3)
print(f"A média aritmética das três notas é:{media}")