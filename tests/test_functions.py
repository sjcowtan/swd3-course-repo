# test addition
def test_addition_int():
  assert addition(4, 7) == 4 # special "if"; if true, continue, else break now

def test_addition_float():
  assert addition(2.3, 7.92) == pytest.approx(10.22, 0.0001)

def test_addition_string():
  assert addition("a", "b") == "Input should be integers or real numbers"

# test squared
def test_squared_odd():
  assert squared(3) == 9

def test_squared_odd():
  assert squared(4) == 16

def test_squared_neg():
  assert squared(-2) > 0

# test square root
## don't need to test for - numbers because sum of squares only
def test_sqroot():
  assert sqroot(9) == 3

# test hypotenuse
def test_hypotenuse():
  assert hypotenuse(3, 4) == 5