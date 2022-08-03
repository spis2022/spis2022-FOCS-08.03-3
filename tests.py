import pytest

from functions import add_em
from functions import factor_limit

#from functions import *

def test_add_em_1():
  assert add_em(2,4)==6

def test_add_em_2():
  assert add_em("UC", "SD")=="UCSD"

def test_add_em_3():
  assert add_em(-100, 100)==0

def test_factor_limit_1():
  assert factor_limit(144)==12

def test_factor_limit_2():
  assert factor_limit(145)==12

def test_factor_limit_3():
  assert factor_limit(143)==11
