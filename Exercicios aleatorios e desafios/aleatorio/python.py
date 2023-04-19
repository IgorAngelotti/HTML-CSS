n = input("Olá, qual o seu nome? -> ")
i = int(input(f"Olá, {n}! Agora nos fale a sua idade: "))
if i > 60:
    print("Você é VELHO!!!")
elif i > 18:
    print("Você é ADULTO!!")
elif i > 12:
    print("Você é ADOLESCENTE!")
else:
    print("Você é CRIANÇA")

v = int(input(f"{n}, agora escolha um valor para fazer a conversão para dolar: "))
r = v*4,98
print(f"US${r}")
