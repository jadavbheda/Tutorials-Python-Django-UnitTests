# unittest framework
* unittest has been built into the Python standard library since version 2.1. You’ll probably see it in commercial Python applications and open-source projects.

* unittest contains both a testing framework and a test runner. unittest has some important requirements for writing and executing tests.

* unittest requires that:
    * You put your tests into classes as methods
    * You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement
    * To convert the earlier example to a unittest test case, you would have to:
        * Import unittest from the standard library
        * Create a class called TestSum that inherits from the TestCase class
        * Convert the test functions into methods by adding self as the first argument
        * Change the assertions to use the self.assertEqual() method on the TestCase class
        * Change the command-line entry point to call unittest.main() OR run with -m unittest

## How to run unittests?
> python test_sum_unittest.py
> python -m unittest test_sum_unittest_runner.py [Preferred]

## Asserts cheat-sheet

| Method        | Checks That           | New In Python Version |
| ------------- |:-------------:| -----:|
| assertEqual(a, b)     | a == b | 
| assertNotEqual(a, b)  | a != b | 
| assertTrue(x)         | bool(x) is True |
| assertFalse(x)        | bool(x) is False |
| assertIs(a, b)        | a is b        | 3.1 | 
| assertIsNot(a, b)     | a is not b    | 3.1 | 
| assertIsNone(x)       | x is None     | 3.1 |
| assertIsNotNone(x)    | x is not None | 3.1| 
| assertIn(a, b)        | a in b        | 3.1 | 
| assertNotIn(a, b)     | a not in b    | 3.1 |
| assertIsInstance(a, b)    | isinstance(a, b)      | 3.2 |
| assertNotIsInstance(a, b) | not isinstance(a, b)  | 3.2 |

