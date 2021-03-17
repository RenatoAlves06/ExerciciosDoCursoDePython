#!python

# 0,1,1,2,3,5,8,13,21...


def fibonacci(limite):
    resultado = [0, 1]
    while resultado[- 1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado


soma = 0
soma = 0
if __name__ == '__main__':
    for fib in fibonacci(1000):
        soma += fib
        print(fib)
    print('Total dos numeros e ', soma)
