def somaDois(a,b):
    return a+b

def somaTres(a,b,c):
    return a+b+c

def somaN(*numeros):
    soma=0
    for n in numeros:
        soma += n
    return soma

if __name__ == '__main__':
    nums = [1,30,3]
    print(somaDois(2,3))
    print(somaTres(*nums))
    print(somaN(2,1,12,3,1,1,23,*nums,3))