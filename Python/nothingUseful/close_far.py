def close_far(a, b, c):
  if abs(a-b) <= 1:
    return(abs(c-a) >= 2 and abs(c-b) >= 2)
  elif abs(a-c) <= 1:
    return(abs(b-a) >= 2 and abs(c-b) >= 2)

print(close_far(1,2,3))