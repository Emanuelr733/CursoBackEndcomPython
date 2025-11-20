mediaf=float(input("Digite a média final do aluno:"))
freq=float(input("Digite a frequência do aluno:"))
aprovado=False
if (mediaf>=7) & (freq>=0.75):
    aprovado=True
print(f"aprovado={aprovado}")