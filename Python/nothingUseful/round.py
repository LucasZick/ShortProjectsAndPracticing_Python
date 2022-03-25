def round_sum(a, b, c):
    newA = round10(a)
    newB = round10(b)
    newC = round10(c)
    return newA + newB + newC

def round10(num):
    if num % 10 == 0:
        return int(num)
    elif num % 5 == 0:
        return int(num+5)
    else:
        return int(round(num/10)*10)

print(round_sum(16,17,18))