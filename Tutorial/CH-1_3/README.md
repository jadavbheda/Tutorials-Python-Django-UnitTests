# Fixtures
* In general fixture is a piece of software or device that sets up a system to satisfy certain preconditions of the process. Its biggest advantage is that it provides consistent results so that the test results can be repeatable. Examples of fixtures could be loading test set to the database, reading a configuration file, setting up environment variables, etc.
* In pytest context, you’d often require data that you want to share across multiple tests. This is done by using objects which are used to instantiate the particular dataset. In pytest, this can be easily done with the help of fixtures.
* Consider a test scenario where MySQL queries are executed on a database. The execution time here depends on the size of the database and the operations can be highly CPU intensive depending on its size. In such cases, repetitive implementation and execution are avoided by using pytest fixtures as they feed data to the tests such as DB connections. 

# Implicit vs Explicit dependency management
* In unittest, you might extract these dependencies into setUp() and tearDown() methods so each test in the class can make use of them. But in doing so, you may inadvertently make the test’s dependence on a particular piece of data or object entirely implicit.
* pytest takes a different approach. It leads you toward explicit dependency declarations that are still reusable thanks to the availability of fixtures.
