# Introduction
This tutorial aims to introduce unit testing in python/django gradually with help of real life examples.

# How to Use this Tutorial
* For each topic in the below list there is a directory with name `CH-<Topic-ID>` under the `Tutorial` directory.
* Each directory contains its own README file and an example (in `src` directory) to explain the topic. 
* Refer README file first and then refer the example.

# Dependencies
Create virtual environment and install dependencies listed in `requirements.txt` file.

    >> virtualenv .venv            
    >> source .venv/bin/activate
    >> pip install -r requirements.txt 

## General rules for testing
[Testing Rules] https://docs.python-guide.org/writing/tests/

## Index
Tutorial covers below topics:
1. Unit testing in Python
    
    1.1. Unittest framework Intro
    1.2. Pytest framework Intro
    1.3. Pytest Features
    
        1.3.1. Fixtures
        1.3.2. Parameterised Test Functions
        
            1.3.2.1. Combining Test Fixtures and Parametrized Test Functions
    
2. Unit testing in Django
    
    2.1. Django's unittest class
    2.2. Pytest with Django 
