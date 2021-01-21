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
        1.3.3. Faker [https://faker.readthedocs.io/en/master/fakerclass.html]
    1.4. Coverage
    
2. Unit testing in Django

    2.1. Django's unittest class
    
    2.2. Pytest with Django 
    
        2.2.0. pytest.ini
        2.2.1. Fixture
        2.2.2. Stub / Mock
        2.2.3. factories
    
    2.3. Subscription API use case
    
        2.3.1. v1 subscription API
        2.3.2. Tests for v1 APIs
        2.3.3. v2 API
        2.3.4. Tests for v2 using DRF features
        
3. EDX Python Tests
