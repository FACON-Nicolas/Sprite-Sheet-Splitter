# Sprite Sheet Splitter

This repository contains the source code of a sprite sheet splitter.
This sprite sheet splitter can split a sprite sheet with `N` rows and `N` columns.

![](https://i.ibb.co/yBpMCzG/Screenshot-2023-08-25-at-22-02-17.png)

# Summary

* **[Summary](#summary)**
* **[Credits](#credits)**
* **[Features](#features)**
  * **[Design Pattern Implementation](#design-pattern-implementation)**
* **[Installation](#installation)**
* **[Version](#version)**

# Credits

* **[FACON Nicolas](https://www.github.com/FACON-Nicolas)** : project creator

# Features

## Design Pattern implementation
This project uses many design patterns:
 + **Singleton** to create only a Window
![](https://miro.medium.com/max/1070/1*GOAK3XdRvjrcpX9dq0fUrQ.png)
 + **decorators** to add splitter and resize on images.
![](https://sourcemaking.com/files/v2/content/patterns/Decorator_example.png)
 + **strategy** to implements many algorithm to split and resize.
![](https://sourcemaking.com/files/v2/content/patterns/Strategy_example1.png)
 + **composite** to save many image with only a method.


![](https://refactoring.guru/images/patterns/diagrams/composite/problem-en.png?id=3320d7ddc5bdc3e43752bb4393710794)

# Installation

```shell
git clone https://github.com/FACON-Nicolas/sprite-sheet-splitter
python3 -m pip install flet
python3 -m pip install pillow
python3 -m pip install deprecated
python3 -m pip install numpy
python3 -m pip install opencv-python
python3 -m pip install scipy
cd sprite-sheet-splitter/
python3 src/Main.py
```

# Version

* **1.0.0**: First Version, developed in November 2022

* **2.0.0**: Second Version, migrate window from Tkinter to Flet, developed in August 2023

