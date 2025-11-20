kg=float(input("Digite seu peso:"))
altura=float(input("Digite sua altura (metros):"))

imc=kg/(altura**2)
if imc < 18.5:
    print("Abaixo do peso")
elif (18.5<=imc) & (imc<25):
    print("Peso normal")
elif (25<=imc) & (imc<30):
    print("Sobrepeso")
elif imc>=30:
    print("Obesidade")