PALAVRAS_PROIBIDAS = {'futebol', 'politica', 'religiao'}
textos = [
    'joao gosta de futebol e politica',
    'A praia foi divertida',
    'Joao gomes na praia',
    'a religiao',
    'conha'
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas: ', intersecao)
    else:
        print('Texto autorizado: ', texto)