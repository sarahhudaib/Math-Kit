---
name: Bug report
about: Create a report to help us improve
title: 'WSL bug report'
labels: 'Cannont render GUI on Ubuntu' 
---


**Describe the bug**
WE faced a bug when we tried to run the program on Ubuntu.


<br>


**To Reproduce**
Steps to reproduce the behavior:
1. Go to the terminal, specifically Ubuntu.
2. Cd into the directory where the program is located.
3. Try to run the program, using the following command:
    ```
    Python main.py
    ```
4. See error:
    ```
    _tkinter.TclError: no display name and no $DISPLAY environment variable
    ```

<br>

**Expected behavior**
The program should not crash, and should output the correct result which is in this case a desktop application of our own. (Math-Kit)


<br>



**Desktop (please complete the following information):**
 - OS: [Windows]
 - Browser [chrome, Brave]


<br>

**Additional context**

We found out the issue existed because WSL or Ubuntu simply doesn't render GUI properly. Therefore. we decided to create a bug report to help us improve the program, and to provide a solution for the bug;

<br>

**Describe the solution**

Instead of using WSL or Ubuntu, it's recommended that the user uses WindowsPowerShell.