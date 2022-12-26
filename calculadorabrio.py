#Calculadora de Briot-Ruffini
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
    else:
        print(f'{raiz} não é uma raiz do polinômio {x3}x³{x2}x²{x1}x{a}')
else:
    print(f'Ainda não conseguimos calcular um polinômio desse grau :(')