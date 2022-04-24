from math_kit import __version__
from math_kit.pages_content.random_generator import RandomGeneratorPage
import numpy as np
import pytest
from math_kit.main import main, Tools


def test_version():
    assert __version__ == '0.1.0'


def test_random_generator_page():
    """          
    This test is to test the GUI of the RandomGeneratorPage.
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.tools == tools
    assert page.randomizer_frame is not None
    assert page.title is not None
    assert page.container is not None
    assert page.box_background_color == tools.pallete["gray"]
    assert page.entries_color == tools.pallete["dark blue"]
    assert page.entry_text_color == tools.pallete["white"]
    assert page.text_color == "black"
    assert page.left_frame is not None
    assert page.left_title is not None
    assert page.length_of_list_label is not None
    assert page.length_of_list_entry is not None
    assert page.right_frame is not None
    assert page.right_title is not None
    assert page.high_label is not None
    assert page.high_entry is not None
    assert page.result_entry is not None
    


def test_random_generator_page_left_frame():
    """             
    This test is to test the GUI of the left frame of the RandomGeneratorPage
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.left_frame is not None
    assert page.left_title is not None
    assert page.length_of_list_label is not None
    assert page.length_of_list_entry is not None


def test_random_generator_page_right_frame():
    """   
    This test is to test the GUI of the right frame of the RandomGeneratorPage          
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.right_frame is not None
    assert page.right_title is not None
    assert page.high_label is not None
    assert page.high_entry is not None




def test_generator_list_method():
    """     
    This test is to test the generator_list method of the RandomGeneratorPage.        
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    page.length_of_list_entry.text = "10"
    page.low_entry.text = "1"
    page.high_entry.text = "10"
    page._GenerateList()
    assert page.result_entry.text is not None


def test_generator_list_method_with_invalid_input():
    """     
    This test is to test the generator_list method of the RandomGeneratorPage.        
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    page.length_of_list_entry.text = "10"
    page.low_entry.text = "1"
    page.high_entry.text = "1"
    page._GenerateList()
    with pytest.raises(ValueError):
        page._GenerateList() 


def test_generator_list_method_with_invalid_input_2():
    """     
    This test is to test the generator_list method of the RandomGeneratorPage.        
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    page.length_of_list_entry.text = "10"
    page.low_entry.text = "10"
    page.high_entry.text = "1"
    page._GenerateList()
    with pytest.raises(ValueError):
        page._GenerateList()



def test_generator_list_method_with_invalid_input_3():

    """     
    This test is to test the generator_list method of the RandomGeneratorPage.        
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    page.length_of_list_entry.text = "10"
    page.low_entry.text = "10"
    page.high_entry.text = "10"
    page._GenerateList()
    with pytest.raises(ValueError):
        page._GenerateList()













