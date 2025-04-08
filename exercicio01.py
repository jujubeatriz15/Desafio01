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