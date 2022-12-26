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
        print(f'{raiz} é uma raiz do polinômio {x3}x³{x2}x²{x1}x{a}')
        #Determinando as outras raízes com a fórmula quadrática 
        raiz2 = ((-an2)+ math.sqrt(an2**2-4*x3*an1))/(2*x3) 
        raiz3 = ((-an2)- math.sqrt(an2**2-4*x3*an1))/(2*x3)
        print(f'As raízes do polinômio {x3}x³{x2}x²{x1}x{a} são: {raiz},{raiz2},{raiz3}')
    else:
        print(f'{raiz} não é uma raiz do polinômio {x3}x³{x2}x²{x1}x{a}')
else:
    print(f'Ainda não conseguimos calcular um polinômio desse grau :(')
