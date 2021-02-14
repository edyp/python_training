"""
Python has it's own types of data:


str
  Examples: "this is a string", f"template-like string with {embedded} variable"

int
  Examples: -1, 0, 1000

bool
  Examples: True, False

dict
  Examples: {'klawiatura': 'keyboard', 'mysz': 'mouse', 'ekran': 'screen'}

list
  Examples: ['MacOSX', 'Linux', 'Windows']


Each type has it's *methods*, things you can do with it, for example:

str
  - "some text".upper()  # Returns "some text"
  - some_words_in_variable.split(' ')  # Returns a list of words, example: ['Those', 'were', 'the', 'words']
  - "michael.jackson".replace('.', ' ').title()  # First replaces dot with space, then uppercases first letter of each word; result: "Michael Jackson"
  - "some" + "text"  # Results in "sometext"

list
  - ['a', 'a', 'b', 'b', 'b', 'c'].count('b')  # Results in 3


We can create our own type (and methods that we can apply to it), by building it from the built-in types:
"""

class Rectangle:
    def __init__(self, a, b):
        # "self" is a storage for all the data you want to keep
        self.a = a
        self.b = b

    def circumference(self):
        return (self.a + self.b) * 2

my_rect = Rectangle(10, 4)
print('The circumference of my rectangle equals', my_rect.circumference())

"""
Make the same for Circle and Triangle
"""
