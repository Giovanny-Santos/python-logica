print("Digite o primeiro valor: ")
valor1 = input()
print("Digite o segundo valor: ")
valor2 = input()
print("Digite o terceiro valor: ")
valor3 = input()

valor1 = int(valor1)
valor2 = int(valor2)
valor3 = int(valor3)

if valor1 > valor2 and valor1 > valor3:
    maior = valor1
    if valor2 > valor3:
        mediano = valor2
        menor = valor3
    else:
        mediano = valor3
        menor = valor2
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
    if valor1 > valor3:
        mediano = valor1
        menor = valor3
    else:
        mediano = valor3
        menor = valor1

if valor3 > valor1 and valor3 > valor2:
    maior = valor3
    if valor1 > valor2:
        mediano = valor1
        menor = valor2
    else:
        mediano = valor2
        menor = valor1

print("O maior valor é: ", maior)
print("O valor mediano é: ", mediano)
print("O menor valor é: ", menor)
        
