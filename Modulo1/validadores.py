email=str(input("Dígite seu email:"))
email = email.strip()
email = email.lower()
if "@" in email:
    print("Email válido")
else:
    print("Email inválido")
print(f"O email formatado é:{email}")