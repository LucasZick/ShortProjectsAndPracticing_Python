def count_code(str):
    count = 0
    if len(str) >= 4:
        for i in range(len(str)-3):
            if str[i:i+2] == 'co' and str[i+3] == 'e':
                count += 1
        return count
    else:
        return 0


print(count_code(''))
