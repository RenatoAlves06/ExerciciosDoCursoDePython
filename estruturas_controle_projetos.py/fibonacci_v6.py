#!python

# 0,1,1,2,3,5,8,13,21...


def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


soma = 0

if __name__ == '__main__':
    for fib in fibonacci(10):  # condição de quantidade de numeros fibonacci
        soma += fib
        print(fib)
    print('Total dos numeros e ', soma)
