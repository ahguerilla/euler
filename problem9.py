def is_tripple(a, b, c):
  lhs = a**2 + b**2
  rhs = c**2
  return lhs == rhs

def problem_nine():
    a = 0
    b = 0
    c = 0
    found_value = False
    while a < 1000 and not found_value:
        a += 1
        b = 0
        while b < 1000 and not found_value:
            b += 1
            c = 1000 - (a + b)
            if is_tripple(a, b, c):
                found_value = True

    if found_value:
      return a * b * c
    else: 
      return 0    

print problem_nine()