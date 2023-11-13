from calculadora import soma

#ISSO E PARA QUANDO APARECER O ERRO, O DEV CONSEGUIR PERCEBER DE CONCRETO O QUE SE ESTA A CONTECER:
try:
    print(soma('1.5', 2.6))
except AssertionError as e:
    print(f'Conta Invalida:{e}')

print(soma(1.31, 20.012))
