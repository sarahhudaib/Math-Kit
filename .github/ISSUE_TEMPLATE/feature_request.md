---
name: Feature request
about: Suggest an idea for this project
title: 'Tests for the project'
labels: 'Cannot test both the GUI and the backend functionality'

---

**Is your feature request related to a problem? Please describe.**

Since we're using tkinter and custom tkinter for our GUI, we needed to be able to test both our GUI and the actual functionality of the program (backend).

But there was an issue of doing so, because the two were not compatible.

<br>

**Describe the solution you'd like**

Sperate the GUI and the backend functionalities into two different classes, each one in a different file and then test them separately.

<br>

**Describe alternatives you've considered**

We tried to write tests for the GUI, and the backend, but the issue was, there was no way to make sure the backend functionalities were working properly. Whereas we could determine that the GUI was working fine.

<br>

