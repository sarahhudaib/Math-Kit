<<<<<<< HEAD
from math_kit.pages_content.stats import StatsPage
import pytest

def test_standard_deviation(test_list):
    pass

@pytest.fixture
=======
from math_kit.pages_content.stats import StatsPage
import pytest
import csv

def test_standard_deviation_list(test_list):
    
    
    actual =4.190954851117173

    expected= StatsPage.standard_deviation_list(test_list)
    assert actual==expected

def test_mean_list(test_list):  
    actual =17.307692307692307

    expected= StatsPage.mean_list(test_list)
    assert actual==expected

def test_median_list(test_list):  
    actual =16
    expected= StatsPage.median_list(test_list)
    assert actual==expected

def test_min_list(test_list):  
    actual =10
    expected= StatsPage.min_list(test_list)
    assert actual==expected

def test_max_list(test_list):  
    actual =23
    expected= StatsPage.max_list(test_list)
    assert actual==expected


def test_standard_deviation_csv(csv_sample):
      
    actual =528.9335834786783
    expected= StatsPage.standard_deviation_csv(csv_sample)
    assert actual==expected

def test_mean_csv(csv_sample):
      
    actual =1061.8393023663452

    expected= StatsPage.mean_csv(csv_sample)
    assert actual==expected

def test_median_csv(csv_sample):
      
    actual =1238.9

    expected= StatsPage.median_csv(csv_sample)
    assert actual==expected

def test_max_csv(csv_sample):
      
    actual =2122.7

    expected= StatsPage.max_csv(csv_sample)
    assert actual==expected

def test_min_csv(csv_sample):
      
    actual =4.190954851117173

    expected= StatsPage.min_csv(csv_sample)
    assert actual==expected




@pytest.fixture
def testing_list():
    testing_list=[10, 12, 23, 23, 16, 23, 21, 16,18,16,14,17,16]
    return testing_list

@pytest.fixture
def csv_sample():
    path=r"math_kit\assets\csv\gold.csv"
    with open(path,"r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        row=next(csv_reader)
        csv_list=list(csv_reader)

        col_list=[]
            
    for row in csv_list:
        col_list.append(float(row["Close"]))

    return col_list
>>>>>>> bac1ca7dce477a1a017afd7881653e8f0c2f49d8
