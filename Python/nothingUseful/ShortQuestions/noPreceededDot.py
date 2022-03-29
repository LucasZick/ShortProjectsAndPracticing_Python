def xyz_there(str):
    if len(str) >= 3:
        for i in range(len(str)):
            if str[i-1] == '.':
                return False
            if str[i:i+3] == 'xyz':
                return True
            else:
                return False

print(xyz_there('xyzdaksdkasa.xyz'))