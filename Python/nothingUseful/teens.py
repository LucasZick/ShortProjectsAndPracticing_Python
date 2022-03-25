def no_teen_sum(a, b, c):
  nums = fix_teen([a,b,c])
  sum = 0
  for n in nums:
    sum += n
  return(sum)

def fix_teen(values):
    fixed_values = []
    for item in values:
        if not((13 <= item <= 19) and not (item == 15) and not (item == 16)):
            fixed_values.append(item)
    return fixed_values


print(no_teen_sum(14, 6, 18))
