import pytest

from functions import add_em
from functions import factor_limit
from functions import first_factor_found

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

def test_first_factor_found_2():
  assert first_factor_found(2)==2

def test_first_factor_found_3():
  assert first_factor_found(3)==3

def test_first_factor_found_4():
  assert first_factor_found(4)==2

def test_first_factor_found_5():
  assert first_factor_found(5)==5

def test_first_factor_found_6():
  assert first_factor_found(2)==2

def test_first_factor_found_9():
  assert first_factor_found(9)==3

def test_first_factor_found_391():
  assert first_factor_found(391)==17
