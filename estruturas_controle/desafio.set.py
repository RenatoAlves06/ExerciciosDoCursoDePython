PALAVRAS_PROIBIDAS = {'Futebol', 'politica', 'futebol'}
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida'
]
for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Este texto possui palavras proibidas como >>', intersecao)

else:
    print('Texto liberado >>', texto)
