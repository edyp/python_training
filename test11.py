import requests
from pprint import pprint
# Using "pip install requests" (in terminal, but not in python imterpreter!)
# Install an external library "requests"
​
# Import it, and using "get" function, make a request to "https://swapi.co/api/" and print the contents
​
# Import "pprint", and using "pprint.pprint(...)" display the same response, but in a nicer way
​
# fill "people" dict will ALL people, not just those from 1st page of results
​
people = {
    # 'name string': 'details dict'
}
​
# Keep asking the user about a name of their favourite character
# if he writes "EXIT", stop the loop and exit the script
# if he writes anythng else, try to find that in "people".
#   if you found it, requests some data about it's homeworld and display it
#   if you could not find it, print "Sorry, try again"
url = 'https://swapi.dev/api/people'
​
while url:
	response = requests.get(url)
	json = response.json()
	for result in json['results']:
		people[result['name']] = result
	url = json['next']
​
while True:
	user_input = input('Who is your favorite character? ')
	if user_input == 'EXIT':
		"Ok, Bye!"
		break

	fav = people.get(user_input, None)
	if fav:
		response2 = requests.get(fav['homeworld'])
		print("{} homeworld is: ".format(user_input))
		pprint(response2.json())
		break
	else:
		print("Sorry, try again")
