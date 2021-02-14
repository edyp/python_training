"""
1. Run:
    pip install pytest
    pip install requests

2. Create a new directory

3. Inside that directory create a file "test_maths.py"

4. Paste the code below in that file:
"""

def working_example():
    assert 5 == 5

def test_failing_example():
    assert 2 == 3

"""
5. Open the console in that directory, and run:
    pytest

6. See that one test fails, fix it

7. See that other test is not being run, fix that (name of test function must start with "test")
"""
