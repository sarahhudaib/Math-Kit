from math_kit import __version__
from math_kit.pages_content.random_generator import RandomGeneratorPage
import numpy as np
import pytest
from main import main, Tools


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
    assert page.high_of_list_label is not None
    assert page.high_of_list_entry is not None
    assert page.result_label is not None
    assert page.result_text is not None
    assert page.result_text_font == ("Helvetica", 18)
    assert page.result_text_bg == tools.pallete["gray"]
    assert page.result_text_fg == tools.pallete["white"]
    assert page.result_text_justify == "center"
    assert page.result_text_width == int(tools.screen_width*0.8)
    assert page.result_text_height == int(tools.screen_height*0.8)


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
    assert page.high_of_list_label is not None
    assert page.high_of_list_entry is not None




def test_generator_list_method():
    """     
    This test is to test the generator_list method of the RandomGeneratorPage.        
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    page.length_of_list_entry.text = "10"
    page.high_of_list_entry.text = "10"
    page.generator_list()
    assert page.result_text.text == "10"
    page.length_of_list_entry.text = "20"
    page.high_of_list_entry.text = "20"
    page.generator_list()
    assert page.result_text.text == "20"
    page.length_of_list_entry.text = "30"
    page.high_of_list_entry.text = "30"
    page.generator_list()
    assert page.result_text.text == "30"
    page.length_of_list_entry.text = "40"
    page.high_of_list_entry.text = "40"
    page.generator_list()
    assert page.result_text.text == "40"
    page.length_of_list_entry.text = "50"
    page.high_of_list_entry.text = "50"
    page.generator_list()
    assert page.result_text.text == "50"
    page.length_of_list_entry.text = "60"
    page.high_of_list_entry.text = "60"
    page.generator_list()
    assert page.result_text.text == "60"
    page.length_of_list_entry.text = "70"
    page.high_of_list_entry.text = "70"
    page.generator_list()
    assert page.result_text.text == "70"
    page.length_of_list_entry.text = "80"
    page.high_of_list_entry.text = "80"
    page.generator_list()
    assert page.result_text.text == "80"
    page.length_of_list_entry.text = "90"

















