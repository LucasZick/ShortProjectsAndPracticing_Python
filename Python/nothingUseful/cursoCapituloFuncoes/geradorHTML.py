def tagBloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'

def tagList(*items):
    lis = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul>{lis}</ul>'

if __name__ == '__main__':
    print('-')
    print (tagBloco('bloco'))
    print (tagBloco('inline e classe', 'info', True))
    print (tagBloco('inline', True))
    print (tagBloco(inline=True, conteudo = 'inline'))
    print (tagBloco('Falhou', classe = 'Error'))
    print('-')
    print (tagBloco(tagList('bruno', 'pedro', 'caio'), classe='List', inline = True))
    print('-')