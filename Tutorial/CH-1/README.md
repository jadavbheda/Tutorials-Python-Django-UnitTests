# What is Unittesting?
Unit testing is a software testing method by which individual units of source code are put under various tests to determine whether they are fit for use. 
It determines and ascertains the quality of your code. Generally, when the development process is complete, the developer codes criteria, or the results that are known to be potentially practical and useful, into the test script to verify a particular unit's correctness. 
During test case execution, various frameworks log tests that fail any criterion and report them in a summary.
The developers are expected to write automated test scripts, which ensures that each and every section or a unit meets its design and behaves as expected.

A unit could be bucketed into various categories:
* An entire module,
* An individual function,
* A complete interface like a class or a method.

The best ways to write unit tests for your code is to first start with a smallest testable unit your code could possibly have, then move on to other units and see how that smallest unit interacts with other units, this way you could build up a comprehensive unit test for your applications.
## Plain Vanilla Test
Writing tests without framework is not easy.

    >> python 1_everything_passes.py 
    >> python 2_not_everything_passes.py 

## Runner or Framework
Test Runner or framework make it easy to write tests.
There are many test runners available for Python. The one built into the Python standard library is called unittest. In this tutorial, you will be using unittest test cases and the unittest test runner. The principles of unittest are easily portable to other frameworks. The three most popular test runners are:

* unittest
* nose or nose2
* pytest

# References 
1. https://docs.python.org/3/library/unittest.html
2. https://www.datacamp.com/community/tutorials/unit-testing-python
3. https://realpython.com/python-testing/
