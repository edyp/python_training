import unittest
import requests

class MathTestCase(unittest.TestCase):
    url_people = 'https://swapi.dev/api/people'
    url_starships = 'https://swapi.dev/api/starships'

    def setUp(self):
        self.films = []
        starship = requests.get(self.url_starships + '/2').json()
        self.films = starship['films']
        print(self.films)

    def tearDown(self):
        pass

    def test_multiplication(self):

        self.assertEqual(2 * 4, 13)

    def test_page1_caracter1_is_luke_skywalker(self):
        people = requests.get(self.url_people).json()['results']
        self.assertEqual(people[0]['name'], 'Luke Skywalker')

unittest.main()
