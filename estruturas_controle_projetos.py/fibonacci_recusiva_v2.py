#!python

# 0,1,1,2,3,5,8,13,21...


def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante : Condição de parada

    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


soma = 0

if __name__ == '__main__':
    for fib in fibonacci(10):  # condição de quantidade de numeros fibonacci
        soma += fib
        print(fib)
    print('Total dos numeros e ', soma)
