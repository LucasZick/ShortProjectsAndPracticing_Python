def count_code(str):
    count = 0
    for i in range(0,len(str)-3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
        return count

print(count_code('codecolecosecopecopecomekoke'))
