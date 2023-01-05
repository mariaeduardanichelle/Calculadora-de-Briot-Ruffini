#Calculadora de Briot-Ruffini
import math
raiz = int(input('Digite a raiz do polinômio: '))
grau = int(input('Digite o grau do seu polinômio: '))
if grau == 3:
    x3 = int(input('Primeiro coeficiente: '))
    x2 = int(input('Segundo coeficiente: '))
    x1 = int(input('Terceiro coeficiente: '))
    a = int(input('Termo independente: '))
    an2 = raiz * x3 + x2
    an1 = raiz * an2 + x1
    an0 = raiz * an1 + a
    if an0 == 0:
        print(f'\n{raiz} é uma raiz do polinômio {x3}x³{x2}x²{x1}x{a}')
        #Determinando as outras raízes com a fórmula quadrática 
        raiz2 = ((-an2)+ math.sqrt(an2**2-4*x3*an1))/(2*x3) 
        raiz3 = ((-an2)- math.sqrt(an2**2-4*x3*an1))/(2*x3)
        print(f'As raízes do polinômio {x3}x³{x2}x²{x1}x{a} são: {raiz},{raiz2},{raiz3}\n')
        #Criando tabela do Briot-Ruffini
        va = ''
        me = '-'*10
        print(f'{raiz:^10}|{x3:^10}|{x2:^10}|{x1:^10}|{a:^10}')
        print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}+{me:^10}')
        print(f'{va:^10}|{x3:^10}|{an2:^10}|{an1:^10}|{an0:^10}\n')
        #Fazendo Briot-Ruffini para a raiz2
        an22 = raiz2 * x3 + an2
        an12 = raiz2 * an22 + an1
        #Criando tabela do Briot-Ruffini para a raiz2
        print(f'{raiz2:^10}|{x3:^10}|{an2:^10}|{an1:^10}')
        print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}')
        print(f'{va:^10}|{x3:^10}|{an22:^10}|{an12:^10}\n') 
        #Fazendo Briot-Ruffini para a raiz3
        an23 = raiz3 * x3 + an22
        #Criando tabela do Briot-Ruffini para a raiz3
        print(f'{raiz3:^10}|{x3:^10}|{an22:^10}')
        print(f'{me:^10}+{me:^10}+{me:^10}')
        print(f'{va:^10}|{x3:^10}|{an23:^10}\n') 
    else:
        print(f'{raiz} não é uma raiz do polinômio {x3}x³{x2}x²{x1}x{a}')
else:
    print(f'Ainda não conseguimos calcular um polinômio desse grau :(')
