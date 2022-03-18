PALAVRAS_PROIBIDAS = ('futebol', 'politica', 'religiao')
textos = [
    'joao gosta de futebol e politica',
    'A praia foi divertida',
    'Joao gomes na praia',
    'a religiao',
    'conha'
]
for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui palavras proibidas: ', palavra)
            break
    
    else:
        print('Texto autorizado:', texto)