import math

def add_em(a, b):
  return a + b

def root1(a, b, c):
  return (-b + math.sqrt(b*b - 4 *a*c))/(2*a)

def root2(a, b, c):
  return (-b - math.sqrt(b*b - 4 *a*c))/(2*a)

def factor_limit(my_integer):
  return int(math.sqrt(my_integer))

def larger(a,b):
  if a>b:
    return a
  else:
    return b

def get_number(prompt):
  return float(input(prompt))
