arquivo = open('pessoas.csv')

try:
    for registro in arquivo:
        print('Nome: {} // Idade: {}'.format(*registro.strip().split(',')))

finally:
    print('Fechando o arquivo...')
    arquivo.close()