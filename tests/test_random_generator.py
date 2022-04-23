from math_kit import __version__
from math_kit.pages_content.random_generator import RandomGeneratorPage
import numpy as np
import pytest
from main import main, Tools


def test_version():
    assert __version__ == '0.1.0'


def test_random_generator_page():
    """             
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
    assert page.result_text_color == tools.pallete["dark blue"]
    assert page.result_text_font == ("Helvetica", 18)
    assert page.result_text_bg == tools.pallete["gray"]
    assert page.result_text_fg == tools.pallete["white"]
    assert page.result_text_justify == "center"
    assert page.result_text_width == int(tools.screen_width*0.8)
    assert page.result_text_height == int(tools.screen_height*0.8)


def test_random_generator_page_left_frame():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.left_frame is not None
    assert page.left_title is not None
    assert page.length_of_list_label is not None
    assert page.length_of_list_entry is not None

def test_random_generator_page_right_frame():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.right_frame is not None
    assert page.right_title is not None
    assert page.high_of_list_label is not None
    assert page.high_of_list_entry is not None

def test_random_generator_page_result_frame():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_label is not None
    assert page.result_text is not None
    assert page.result_text_color == tools.pallete["dark blue"]
    assert page.result_text_font == ("Helvetica", 18)
    assert page.result_text_bg == tools.pallete["gray"]
    assert page.result_text_fg == tools.pallete["white"]
    assert page.result_text_justify == "center"
    assert page.result_text_width == int(tools.screen_width*0.8)
    assert page.result_text_height == int(tools.screen_height*0.8)


def test_random_generator_page_left_frame_title():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.left_title is not None
    assert page.left_title.text == "Length of List"
    assert page.left_title.font == ("Helvetica", 18)
    assert page.left_title.bg == tools.pallete["gray"]
    assert page.left_title.fg == tools.pallete["dark blue"]
    assert page.left_title.justify == "center"
    assert page.left_title.width == int(tools.screen_width*0.2)
    assert page.left_title.height == int(tools.screen_height*0.05)

def test_random_generator_page_left_frame_length_of_list_entry():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.length_of_list_entry is not None
    assert page.length_of_list_entry.text == "10"
    assert page.length_of_list_entry.font == ("Helvetica", 18)
    assert page.length_of_list_entry.bg == tools.pallete["gray"]
    assert page.length_of_list_entry.fg == tools.pallete["dark blue"]
    assert page.length_of_list_entry.justify == "center"
    assert page.length_of_list_entry.width == int(tools.screen_width*0.2)
    assert page.length_of_list_entry.height == int(tools.screen_height*0.05)


def test_random_generator_page_right_frame_title():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.right_title is not None
    assert page.right_title.text == "High of List"
    assert page.right_title.font == ("Helvetica", 18)
    assert page.right_title.bg == tools.pallete["gray"]
    assert page.right_title.fg == tools.pallete["dark blue"]
    assert page.right_title.justify == "center"
    assert page.right_title.width == int(tools.screen_width*0.2)
    assert page.right_title.height == int(tools.screen_height*0.05)


def test_random_generator_page_right_frame_high_of_list_entry():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.high_of_list_entry is not None
    assert page.high_of_list_entry.text == "10"
    assert page.high_of_list_entry.font == ("Helvetica", 18)
    assert page.high_of_list_entry.bg == tools.pallete["gray"]
    assert page.high_of_list_entry.fg == tools.pallete["dark blue"]
    assert page.high_of_list_entry.justify == "center"
    assert page.high_of_list_entry.width == int(tools.screen_width*0.2)
    assert page.high_of_list_entry.height == int(tools.screen_height*0.05)

def test_random_generator_page_result_frame_title():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_label is not None
    assert page.result_label.text == "Result"
    assert page.result_label.font == ("Helvetica", 18)
    assert page.result_label.bg == tools.pallete["gray"]
    assert page.result_label.fg == tools.pallete["dark blue"]
    assert page.result_label.justify == "center"
    assert page.result_label.width == int(tools.screen_width*0.2)
    assert page.result_label.height == int(tools.screen_height*0.05)

def test_random_generator_page_result_frame_result_text():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text is not None
    assert page.result_text.text == "10"
    assert page.result_text.font == ("Helvetica", 18)
    assert page.result_text.bg == tools.pallete["gray"]
    assert page.result_text.fg == tools.pallete["dark blue"]
    assert page.result_text.justify == "center"
    assert page.result_text.width == int(tools.screen_width*0.8)
    assert page.result_text.height == int(tools.screen_height*0.8)

def test_random_generator_page_result_frame_result_text_color():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_color == tools.pallete["dark blue"]


def test_random_generator_page_result_frame_result_text_font():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_font == ("Helvetica", 18)

def test_random_generator_page_result_frame_result_text_bg():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_bg == tools.pallete["gray"]


def test_random_generator_page_result_frame_result_text_fg():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_fg == tools.pallete["white"]

def test_random_generator_page_result_frame_result_text_justify():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_justify == "center"

def test_random_generator_page_result_frame_result_text_width():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_width == int(tools.screen_width*0.8)



def test_random_generator_page_result_frame_result_text_height():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_height == int(tools.screen_height*0.8)

def test_random_generator_page_result_frame_result_text_color():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_color == tools.pallete["dark blue"]

def test_random_generator_page_result_frame_result_text_font():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_font == ("Helvetica", 18)

def test_random_generator_page_result_frame_result_text_bg():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_bg == tools.pallete["gray"]

def test_random_generator_page_result_frame_result_text_fg():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_fg == tools.pallete["white"]


def test_random_generator_page_result_frame_result_text_justify():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_justify == "center"

def test_random_generator_page_result_frame_result_text_width():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_width == int(tools.screen_width*0.8)


def test_random_generator_page_result_frame_result_text_height():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_height == int(tools.screen_height*0.8)


def test_random_generator_page_result_frame_result_text_color():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_color == tools.pallete["dark blue"]


def test_random_generator_page_result_frame_result_text_font():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_font == ("Helvetica", 18)


def test_random_generator_page_result_frame_result_text_bg():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_bg == tools.pallete["gray"]


def test_random_generator_page_result_frame_result_text_fg():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_fg == tools.pallete["white"]


def test_random_generator_page_result_frame_result_text_justify():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_justify == "center"


def test_random_generator_page_result_frame_result_text_width():
    """             
    """
    tools = Tools()
    page = RandomGeneratorPage(None, tools)
    assert page.result_text_width == int(tools.screen_width*0.8)

    

