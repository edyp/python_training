import requests

url = 'https://swapi.dev/api/people'

people = requests.get(url).json()['results']

homeworlds = {

}
planets_seen = []

for character in people:
    url = character['homeworld']
    if url not in planets_seen:
        homeworld = requests.get(url).json()
        homeworlds[character['name'] + '\'s homeworld'] = homeworld['name']
        planets_seen.append(url)

print(homeworlds)
