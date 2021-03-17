palavra = 'paralelepipeto'
for letra in palavra:
        print(letra, end=' , ')
print('FIM')

Aprovados = ['Rafaela', 'Gil', 'Lais', 'Tia']
for nome in Aprovados:
    print(nome, end=',')

for posicao, nome in enumerate(Aprovados):
    print('\n',f' {posicao + 1})', nome)

dias_semana = ('segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
for dia in dias_semana:
    print('Hoje e ' + dia)

for numero in{1, 2, 3, 4, 5, 6}:
    print(numero)

for num in set('1,2,3,4,5,6,7,8'):
    print(num)
print('\n')
for let in set('Vai Da Tudo Certo'):
    print(let)
