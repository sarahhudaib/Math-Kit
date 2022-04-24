# **Math Kit**

[Math Kit](https://github.com/sarahhudaib/Math-Kit) is a GUI desktop app, that is made specifically for performing basic and advanced mathematical operations  (as will be mentioned below)  without any additional hassle as it insures that it serves the main purpose of providing a top-tier mathematical help with not much spent effort by the user.

<br>

## **Math Kit features**:

The provided features by the GUI tool are the following:

- **Home Page:** This window or page is used display brief information about the project and a simple guide on how to use it.

- **Workspace Page:** This window is where all the mathematical operations will be carried out, as it contains cards for each one of the following operations:      
    - ***Calculator:*** performs a few simple and a bit more advanced operations, such as: addition, subtraction, multiplication, division, square root of a number, log of a number, and the trigonometric functions including the hyperbolic trigonometry.
    - ***Plotter:*** demonstrates the plot or the graph for an equation that's entered by the user.
    - ***Convertor:*** performs unit conversions between various common units of measurements
    - ***Randomizer:*** generates random lists and numbers for a given input entered by the user.
    - ***Statistics:*** performs mathematical operations relating to a given set or data, such as: mean, median, standard deviation.
    - ***Calculus:*** performs more complex mathematical operations, such as: derivation and integration
    - ***Numerical:*** performs other type of mathematical operations, such as: Newton Raphson Method 

- **Team Info:** This window is for showing more information about the developers behind this project.
- **Settings:** This window is for controlling a few characteristics of the GUI.

<br>

## **Planning of the Project**

[The Project Layout on Replit ](https://replit.com/@MustafaAlhasana/mid#mid%20draw%20.draw)

<br>

## **Wireframe**

<br>



## **Project Directory Tree**
```
├── math_kit
│   ├── assets
|   |    |── avatars
│   |    |  ├── batool.png
│   |    |  ├── mustafa.png
│   |    |  ├── salim.png
│   |    |  └── sara.png
│   |    |── csv
│   |    |  ├── data.csv
│   |    |  └── gold.csv
│   |    |── icons
│   |    |  ├── calc.png
│   |    |  ├── clear.png
│   |    |  ├── convert.png
│   |    |  ├── diff.png
│   |    |  ├── flip.png
│   |    |  ├── numeric.png
│   |    |  ├── plot.png
│   |    |  ├── random.png
│   |    |  └── stats.png
│   |    |── plots
│   |    |  └── plot.png
│   |    |── sounds
│   |    |  ├── card_click.wav
│   |    |  └── navigate_click.wav
│   ├── pages_content
│   │    ├── derive_and_integrate.py
│   │    ├── home.py
│   │    ├── main_page.py
│   │    ├── numerical_operations.py
│   │    ├── plotting.py
│   │    ├── random_generator.py
│   │    ├── scienfitic_calculator.py
│   │    ├── settings.py
│   │    ├── stats.py
│   │    ├── team_info.py
│   │    ├── unit_converter.py
|   |    └── workspace.py
|   ├── main.py
|   ├── tempCodeRunnerFile.py
├── tests
│   ├── test_GUI
│   |    ├── test_ask_open_file.py
│   |    ├── test_grid.py
│   |    ├── test_horizontal_scale.py
│   |    ├── test_label_button.py
│   |    ├── test_question_icon.py
│   |    └── test_top_level_widget.py
│   ├── test_image
│   |    └── blue.png
|   ├── __init__.py
|   ├── test_random_generator.py
|   ├── test_scientific_calc.py
|   ├── test_statistics.py
|   ├── 
|   ├── 
├── .gitignore 
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.md
└── work_space_cards.md
```

<br>

## **Used Libraries and Tools**

- **VS Code** 
- **Python** 
- **Tkinter** 
- **Pillow** 
- **Pytest**
- **Poetry**
- **NumPy**
- **Replit** 
- **webbrowser** 
- **threading**
- **playsound**
- **black**

<br>


## **A Guide to Getting Started**
```
Clone this repository to your local machine, by following this command:

`$ git clone git@github.com:sarahhudaib/Math-Kit.git`

---------------------------------------------------------------

Navigate to the repo's directory and install required  dependencies:

`$ poetry install`
`$ pip install --upgrade pip`
`$ pip install Pillow`
`$ pip install numpy`
`$ pip install matplotlib`
`$ -m pip install -U black` 
`$ pip install playsound`




---------------------------------------------------------------

Open the repo in a text editor of your choice. In our case, we're assuming you're using VS Code:

`$ code .`

---------------------------------------------------------------

Activate the virtual environment:

`$ poetry shell`

---------------------------------------------------------------

Important notes:

1. For extra careful measures; when running the program make sure you have the latest updated version of python installed on your local machine (Python 3.10.1), specifically on Windows, you can use the following command:

`$ python -m pip install --upgrade pip`


2. Activate the virtual environment by running the following command:

`$ poetry shell`

definatly after install poetry, using this command:

`$ poetry install`

3. Navigate inside "Math-Kit\math_kit" directory to run the program, preferably on "Windows Powershell" not "Ubuntu" and that's because WSL doesn't support rendering GUI, so it's advised to be careful as to not run into some issues you want to stay away from.

4. After cd'ing inside the above directory, and after activating the virtual environment, run this command 

`$ python main.py`

This will render a GUI window on your local machine, that has all the above mentioned features that you could navigate through very easily to perform any kind of mathematical operation.

---------------------------------------------------------------
```

