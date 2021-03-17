#!python

# 0,1,1,2,3,5,8,13,21...


def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


soma = 0

if __name__ == '__main__':
    for fib in fibonacci(20):  # condição de quantidade de numeros fibonacci
        soma += fib
        print(fib)

    print('Soma dos numeros e =', soma)
