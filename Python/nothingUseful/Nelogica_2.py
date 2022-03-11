import sys


names = ['jackson', 'jacques', 'jack']
query = 'jack'

try:
    queryPassed = []
    queryNotPassed = []

    for i in names:
        if query in i[0:len(query)] and query in i[0:-1]:
            queryPassed.append(names.index(i)+1)
        else:
            queryNotPassed.append(names.index(i)+1)

    for i in queryPassed:
        sys.stdout.write(str(i)+' ')
    sys.stdout.write('\n')


    for i in queryNotPassed:
        sys.stdout.write(str(i)+' ')
    sys.stdout.write('\n')
except Exception as error:
    sys.stdout.write(error)