from datetime import datetime
begin = datetime.now()

lista = [12,3,12,31,3,213,1,31,2,13,13,2,13,1,32,3,123]
soma = 0
for i in lista:
    soma = soma + i

timer = datetime.now() - begin
print('tempo for: '+str(timer))
##################################
begin = datetime.now()
soma = 0
i=0
while i < len(lista):
    soma = soma + i
    i = i + 1

timer = datetime.now() - begin
print(timer)
print('tempo while: '+str(timer))