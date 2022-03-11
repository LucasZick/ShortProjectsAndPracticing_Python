a = 'lucas'
b = 'zic'

if len(a)<=len(b):
    bigger = len(b)
else:
    bigger = len(a)

password = []

for i in range(bigger):
    if a:
        password.append(a[0])
        a = a[1:]
    else:
        pass
    if b:
        password.append(b[0])
        b = b[1:]
    else:
        pass
password = ''.join(map(str,password))
print(password)