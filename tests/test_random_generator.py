from math_kit import __version__
from math_kit.pages_content.random_generator import RandomGeneratorPage
import numpy as np


def test_version():
    assert __version__ == '0.1.0'


def test_length_of_list():
    generator = RandomGeneratorPage(None, None)
    length_of_list_threshold = 5
    seed_threshold = 4
    high_threshold = 7
    random_list = np.random.randint(low= seed_threshold, high=high_threshold, size=length_of_list_threshold)
    assert len(random_list) == length_of_list_threshold

def test_seed_of_list():
    generator = RandomGeneratorPage(None, None)
    length_of_list_threshold = 5
    seed_threshold = 4
    high_threshold = 7
    random_list = np.random.randint(low= seed_threshold, high=high_threshold, size=length_of_list_threshold)
    assert random_list[0] == seed_threshold

def test_high_of_list():
    generator = RandomGeneratorPage(None, None)
    length_of_list_threshold = 5
    seed_threshold = 4
    high_threshold = 7
    random_list = np.random.randint(low= seed_threshold, high=high_threshold, size=length_of_list_threshold)
    assert random_list[-1] == high_threshold

def test_seed_and_high_of_list():
    generator = RandomGeneratorPage(None, None)
    length_of_list_threshold = 5
    seed_threshold = 4
    high_threshold = 7
    random_list = np.random.randint(low= seed_threshold, high=high_threshold, size=length_of_list_threshold)
    assert random_list[0] == seed_threshold
    assert random_list[-1] == high_threshold
