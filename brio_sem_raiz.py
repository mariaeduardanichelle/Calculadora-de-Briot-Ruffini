import math
grau = int(input('Digite o grau do polinômio: '))
if grau == 3:
  x3 = int(input('Digite o primeiro coeficiente: '))
  x2 = int(input('Digite o segundo coeficiente: '))
  x1 = int(input('Digite o terceiro coeficiente: '))
  a = int(input('Digite o termo independente: '))
  if x3 > 0 and a < 0:
    for c in range(1, x3+1):
      if x3 % c == 0:
        for i in range(a, 0):
          if a % i == 0:
            praiz = i/c
            nraiz = -(i/c)
            ap2 = praiz * x3 + x2
            ap1 = praiz * ap2 + x1
            ap0 = praiz * ap1 + a
            an2 = nraiz * x3 + x2
            an1 = nraiz * an2 + x1
            an0 = nraiz * an1 + a
            if ap0 == 0:
              raiz = praiz
            if an0 == 0:
              raiz = nraiz
              raiz2 = ((-an2)+ math.sqrt(an2**2-4*x3*an1))/(2*x3) 
              raiz3 = ((-an2)- math.sqrt(an2**2-4*x3*an1))/(2*x3)
              print(f'\nAs raízes do polinômio {x3}x³{x2}x²{x1}x{a} são: {raiz}, {raiz2}, {raiz3}\n')
              va = ''
              me = '-'*10
              print(f'{raiz:^10}|{x3:^10}|{x2:^10}|{x1:^10}|{a:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an2:^10}|{an1:^10}|{an0:^10}\n')
              an22 = raiz2 * x3 + an2
              an12 = raiz2 * an22 + an1
              print(f'{raiz2:^10}|{x3:^10}|{an2:^10}|{an1:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an22:^10}|{an12:^10}\n') 
              an23 = raiz3 * x3 + an22
              print(f'{raiz3:^10}|{x3:^10}|{an22:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an23:^10}\n')
  if x3 > 0 and a > 0:
    for c in range(1, x3+1):
      if x3 % c == 0:
        for i in range(1, a+1):
          if a % i == 0:
            praiz = i/c
            nraiz = -(i/c)
            ap2 = praiz * x3 + x2
            ap1 = praiz * ap2 + x1
            ap0 = praiz * ap1 + a
            an2 = nraiz * x3 + x2
            an1 = nraiz * an2 + x1
            an0 = nraiz * an1 + a
            if ap0 == 0:
              raiz = praiz
            if an0 == 0:
              raiz = nraiz
              raiz2 = ((-an2)+ math.sqrt(an2**2-4*x3*an1))/(2*x3) 
              raiz3 = ((-an2)- math.sqrt(an2**2-4*x3*an1))/(2*x3)
              print(f'\nAs raízes do polinômio {x3}x³{x2}x²{x1}x{a} são: {raiz}, {raiz2}, {raiz3}\n')
              va = ''
              me = '-'*10
              print(f'{raiz:^10}|{x3:^10}|{x2:^10}|{x1:^10}|{a:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an2:^10}|{an1:^10}|{an0:^10}\n')
              an22 = raiz2 * x3 + an2
              an12 = raiz2 * an22 + an1
              print(f'{raiz2:^10}|{x3:^10}|{an2:^10}|{an1:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an22:^10}|{an12:^10}\n') 
              an23 = raiz3 * x3 + an22
              print(f'{raiz3:^10}|{x3:^10}|{an22:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an23:^10}\n')
  if x3 < 0 and a < 0:
    for c in range(x3, 0):
      if x3 % c == 0:
        for i in range(a, 0):
          if a % i == 0:
            praiz = i/c
            nraiz = -(i/c)
            ap2 = praiz * x3 + x2
            ap1 = praiz * ap2 + x1
            ap0 = praiz * ap1 + a
            an2 = nraiz * x3 + x2
            an1 = nraiz * an2 + x1
            an0 = nraiz * an1 + a
            if ap0 == 0:
              raiz = praiz
            if an0 == 0:
              raiz = nraiz
              raiz2 = ((-an2)+ math.sqrt(an2**2-4*x3*an1))/(2*x3) 
              raiz3 = ((-an2)- math.sqrt(an2**2-4*x3*an1))/(2*x3)
              print(f'\nAs raízes do polinômio {x3}x³{x2}x²{x1}x{a} são: {raiz}, {raiz2}, {raiz3}\n')
              va = ''
              me = '-'*10
              print(f'{raiz:^10}|{x3:^10}|{x2:^10}|{x1:^10}|{a:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an2:^10}|{an1:^10}|{an0:^10}\n')
              an22 = raiz2 * x3 + an2
              an12 = raiz2 * an22 + an1
              print(f'{raiz2:^10}|{x3:^10}|{an2:^10}|{an1:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an22:^10}|{an12:^10}\n') 
              an23 = raiz3 * x3 + an22
              print(f'{raiz3:^10}|{x3:^10}|{an22:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an23:^10}\n')
  if x3 < 0 and a > 0:
    for c in range(x3, 0):
      if x3 % c == 0:
        for i in range(1, a+1):
          if a % i == 0:
            praiz = i/c
            nraiz = -(i/c)
            ap2 = praiz * x3 + x2
            ap1 = praiz * ap2 + x1
            ap0 = praiz * ap1 + a
            an2 = nraiz * x3 + x2
            an1 = nraiz * an2 + x1
            an0 = nraiz * an1 + a
            if ap0 == 0:
              raiz = praiz
            if an0 == 0:
              raiz = nraiz
              raiz2 = ((-an2)+ math.sqrt(an2**2-4*x3*an1))/(2*x3) 
              raiz3 = ((-an2)- math.sqrt(an2**2-4*x3*an1))/(2*x3)
              print(f'\nAs raízes do polinômio {x3}x³{x2}x²{x1}x{a} são: {raiz}, {raiz2}, {raiz3}\n')
              va = ''
              me = '-'*10
              print(f'{raiz:^10}|{x3:^10}|{x2:^10}|{x1:^10}|{a:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an2:^10}|{an1:^10}|{an0:^10}\n')
              an22 = raiz2 * x3 + an2
              an12 = raiz2 * an22 + an1
              print(f'{raiz2:^10}|{x3:^10}|{an2:^10}|{an1:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an22:^10}|{an12:^10}\n') 
              an23 = raiz3 * x3 + an22
              print(f'{raiz3:^10}|{x3:^10}|{an22:^10}')
              print(f'{me:^10}+{me:^10}+{me:^10}')
              print(f'{va:^10}|{x3:^10}|{an23:^10}\n')
else:
  print(f'Ainda não conseguimos calcular polinômios de grau {grau}')
