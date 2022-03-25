def execute(funcao):
    if callable(funcao):
        funcao()
    else:
        print('Não é uma função')

def bomDia():
    print ('Bom dia')

def boaTarde():
    print ('Boa tarde')

if __name__ == '__main__':
    execute(bomDia)
    execute(boaTarde)