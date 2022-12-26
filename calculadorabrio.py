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
        #Criando tabela do Briot-Ruffini
        linha1 = [raiz, x3, x2, x1, a]
        linha12 = [x3, an2, an1, an0]
        print('{:^6}   {:^13}   {:^13}   {:^13}   {:^13}'.format(*linha1))
        print('         {:^13}   {:^13}   {:^13}   {:^13}'.format(*linha12))
        #Fazendo Briot-Ruffini para a raiz2
        an22 = raiz2 * x3 + an2
        an12 = raiz2 * an22 + an1
        linha2 = [raiz2, x3, an2, an1]
        linha22 = [x3, an22, an12]
        #Criando tabela do Briot-Ruffini para a raiz2
        print('{:^6}   {:^13}   {:^13}   {:^13}'.format(*linha2))
        print('         {:^13}   {:^13}   {:^13}'.format(*linha22)) 
        #Fazendo Briot-Ruffini para a raiz3
        an23 = raiz3 * x3 + an22
        linha3 = [raiz3, x3, an22]
        linha32 = [x3, an23]
        #Criando tabela do Briot-Ruffini para a raiz3
        print('{:^6}   {:^13}   {:^13}'.format(*linha3))
        print('         {:^13}   {:^13}'.format(*linha32)) 
    else:
        print(f'{raiz} não é uma raiz do polinômio {x3}x³{x2}x²{x1}x{a}')
else:
    print(f'Ainda não conseguimos calcular um polinômio desse grau :(')
