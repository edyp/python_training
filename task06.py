"""
You can parametrize the test to run the same code with different data.
"""

import pytest

@pytest.mark.parametrize("number", [10, 20, 100, 1001])
def test_number_is_divisible_by_10(number):
    assert number % 10 == 0

"""
Rewite "pilots" test so that it accepts a name of the pilot as a parameter (like above)

Example:
@pytest.mark.parametrize('pilot_name', ['Han Solo', 'Chewbacca', ...])
"""
