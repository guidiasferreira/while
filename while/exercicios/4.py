
numero_funcionario = int(input("Entre com o número de funcionários: "))

inicial = 1 
soma_salario = 0
maior_salario = 0
menor_salario = 100000

while inicial <= numero_funcionario:
    salario = float(input(f"Entre com o salário do funcionário {inicial}\u00BA: "))
    soma_salario = soma_salario + salario
    media = soma_salario / numero_funcionario

    if salario > maior_salario:
        maior_salario = salario

    elif salario < menor_salario:
        menor_salario = salario

    inicial = inicial + 1

print(f"A soma dos salários = {soma_salario :.2f}")
print(f"A média salarial = {media :.2f}")
print(f"O maior salário = {maior_salario:.2f}")
print(f"O menor salário = {menor_salario:.2f}")