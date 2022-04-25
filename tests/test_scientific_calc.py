from math_kit import __version__
from math_kit.pages_content.scientific_calculator import ScientificCalculator

def test_version():
    assert __version__ == '0.1.0'

def test_add():
    calculator = ScientificCalculator()
    assert calculator.add(1, 2) == 3
    
def test_subtract():
    calculator = ScientificCalculator()
    assert calculator.subtract(2, 1) == 1

def test_multiply():
    calculator = ScientificCalculator()
    assert calculator.multiply(2, 2) == 4

def test_divide():
    calculator = ScientificCalculator()
    assert calculator.divide(4, 2) == 2
    
def test_square():
    calculator = ScientificCalculator()
    assert calculator.square(2) == 4
    
def test_square_root():
    calculator = ScientificCalculator()
    assert calculator.square_root(4) == 2
    
def test_cube():
    calculator = ScientificCalculator()
    assert calculator.cube(2) == 8
    
def test_cube_root():
    calculator = ScientificCalculator()
    assert calculator.cube_root(8) == 2
    
def test_exponent():
    calculator = ScientificCalculator()
    assert calculator.exponent(2, 2) == 4
    
def test_log():
    calculator = ScientificCalculator()
    assert calculator.log(2, 2) == 1
    
def test_sin():
    calculator = ScientificCalculator()
    assert calculator.sin(2) == 0.9092974268256817
    
def test_cos():
    calculator = ScientificCalculator()
    assert calculator.cos(2) == -0.4161468365471424
    
def test_tan():
    calculator = ScientificCalculator()
    assert calculator.tan(2) == -1.5574077246549023
    
def test_sinh():
    calculator = ScientificCalculator()
    assert calculator.sinh(2) == 3.626860407847019
    
def test_cosh():
    calculator = ScientificCalculator()
    assert calculator.cosh(2) == 1.5430806348152437
    
def test_tanh():
    calculator = ScientificCalculator()
    assert calculator.tanh(2) == 0.4636476090008061
    
def test_factorial():
    calculator = ScientificCalculator()
    assert calculator.factorial(2) == 2
    
def test_pi():
    calculator = ScientificCalculator()
    assert calculator.pi() == 3.141592653589793
    
def test_e():
    calculator = ScientificCalculator()
    assert calculator.e() == 2.718281828459045
    
def test_e_to_the_power_of_x():
    calculator = ScientificCalculator()
    assert calculator.e_to_the_power_of_x(2) == 7.38905609893065
    
def test_x_to_the_power_of_e():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_e(2) == 7.38905609893065
    
def test_x_to_the_power_of_y():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(2, 2) == 4.0
    
def test_x_to_the_power_of_y_with_negative_y():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(2, -2) == 0.25
    
    
def test_x_to_the_power_of_y_with_negative_x():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(-2, 2) == -4.0
    
def test_x_to_the_power_of_y_with_negative_x_and_y():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(-2, -2) == 0.25
    
def test_x_to_the_power_of_y_with_zero_x():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(0, 2) == 0.0
    
def test_x_to_the_power_of_y_with_zero_y():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(2, 0) == 1.0
    
def test_x_to_the_power_of_y_with_zero_x_and_y():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(0, 0) == 1.0
    
def test_x_to_the_power_of_y_with_negative_x_and_zero_y():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(-2, 0) == 1.0
    
def test_x_to_the_power_of_y_with_zero_x_and_negative_y():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(0, -2) == 1.0
    
def test_x_to_the_power_of_y_with_negative_x_and_negative_y():
    calculator = ScientificCalculator()
    assert calculator.x_to_the_power_of_y(-2, -2) == 0.25



