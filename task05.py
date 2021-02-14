"""
1. At the top of "test_millenium_falcon.py" paste the code:
"""

import pytest

@pytest.fixture
def url_of_falcon():
    return "https://swapi.co/api/starships/10/"


"""
2. Change the test functions to have an argument named exactly like the function above:
    Example:
    def test_pilots_or_however_you_called_that_test(url_of_falcon):



3. Replace occurences of the starship url with url_of_falcon

4. The tests should still pass

Pytest will look at function arguments' names and provide values from fixtures with the same name.

In this example, it will see that the "test_pilots" function needs "url_of_falcon"
it will look for a fixture of that name,
and use it's return value (the string "https://.../10/") in the test
"""
