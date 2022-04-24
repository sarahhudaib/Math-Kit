from math_kit.pages_content.stats import StatsPage
import pytest

def test_standard_deviation(test_list):
    
    StatsPage.statistics_list(test_list)
    actual =4.0265391779392

    expected= StatsPage.statistics_list(test_list)
    assert actual==expected

@pytest.fixture
def test_list():
    testing_list=[10, 12, 23, 23, 16, 23, 21, 16,18,16,14,17,16]
    return testing_list