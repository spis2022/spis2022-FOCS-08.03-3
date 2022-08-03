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

def first_factor_found(my_number):
  """
  if number is prime, just return the number
  otherwise return the first factor other than 1
  that can be found (smallest factor)
  """
  
  for i in range(2, factor_limit(my_number) + 1):
    if my_number % i == 0:
      return i
  
  return my_number

def is_prime(number):
  return first_factor_found(number)==number