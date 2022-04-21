# **Math Kit**

[Math Kit](https://github.com/sarahhudaib/Math-Kit) is an advanced GUI tool, that is made specifically for performing basic and advanced mathematical operations  (as will be mentioned below)  without any additional hassle as it insures that it serves the main purpose of providing a top-tier mathematical help with not much spent effort by the user.

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
.
├── LICENSE
├── README.md
├── math_kit
│   ├── assets
|   |  |── avatars
│   |      ├── batool.png
│   |      ├── mustafa.png
│   |      ├── salim.png
│   |      └──  sara.png
│   │── pages_content
|   |  |── __pycache__
│   │  |    ├── home.cpython-39.pyc
│   │  |    ├── home.cpython-310.pyc
│   │  |    ├── main_page.cpython-39.pyc
│   │  |    ├── main_page.cpython-310.pyc
│   │  |    ├── settings.cpython-39.pyc
│   │  |    ├── settings.cpython-310.pyc
│   │  |    ├── team_info.cpython-39.pyc
│   │  |    ├── team_info.cpython-310.pyc
│   │  |    ├── workspace.cpython-39.pyc
|   |  |    └── workspace.cpython-310.pyc
│   ├  |── derive_and_integrate.py
|   |  ├── home.py
│   |  ├── main_page.py
│   |  ├── numerical_operations.py
│   |  ├── plotting.py
│   |  ├── random_generator.py
│   |  ├── scienfitic_calculator.py
│   |  ├── settings.py
│   |  ├── stats.py
│   |  ├── team_info.py
│   |  ├── unit_converter.py
│   |  └── workspace.py
|   |── main.py
|   |── tempCodeRunnerFile.py
├── poetry.lock
├── pyproject.toml
├── tests
    ├── __init.py__
    │   
    │  
└── README.md

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



---------------------------------------------------------------

Open the repo in a text editor of your choice. In our case, we're assuming you're using VS Code:

`$ code .`

---------------------------------------------------------------

Activate the virtual environment:

`$ poetry shell`

---------------------------------------------------------------

Important notes:

1. For extra careful measures; when running the program make sure you have the latest updated version of python installed on your local machine (Python 3.10.1).

2. Navigate inside "Math-Kit\math_kit" directory to run the program, preferably on "Windows Powershell" not "Ubuntu" and that's because WSL doesn't support rendering GUI and that could lead to some issues we want to stay away from.

3. After cd'ing inside the above directory, and after activating the virtual environment, run this command 

`$ python main.py`

This will render a GUI window on your local machine, that has all the above mentioned features that you could navigate through very easily to perform any kind of mathematical operation.

---------------------------------------------------------------
```

