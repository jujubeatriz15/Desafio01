<<<<<<< HEAD
#atividade do dia 01/04
nome = input("digite seu nome ")
idade = int(input("digite sua idade "))
salario = float(input("qual o seu salario: "))
aumento = float(input("qual foi o percentual do seu aumento: "))
valorReal = salario*aumento/100
novoSalario = salario+valorReal
print(f"Ola {nome} sua idade é {idade} e seu salario é {salario}")
print(f"Seu aumento foi {novoSalario}")
=======
#exercicio01
h01 = int(input("Digite a Hora1" ))
m01 = int(input("Digite a Hora2" ))
h02 = int(input("Digite a Hora2" ))
m02 = int(input("Digite a Hora2" ))

somaH = h01 + m01
somaH = h02 + m02

if somaH>59:
    somaH+=1
    somaH = somaH - 60
if somaH>=36:
    somaH-=36
elif somaH>=24:
    somaH = somaH - 24
elif somaH>=12:
    somaH = somaH - 12
print(somaH,somaH)
>>>>>>> d20b2736ebec4de5463084fa96644f3c6a3a9c26
