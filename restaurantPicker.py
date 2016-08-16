#Restaurant Picker using Yelp API

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io
import json

# read API keys
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

query = raw_input("What kind of restaurant would you like? ")
location = raw_input("Please enter a location for the search: ")
distance = raw_input("What is the search radius (in meters)? ")

params = {
	'term': query,
	'sort': 2,
	'radius_filter': distance
}

result = client.search(location, **params)

loc = ""
for restaurant in result.businesses:
	loc = ""
	print "Name: %s" %restaurant.name
	print "Location: "
	for value in restaurant.location.display_address:
		if(loc == ""):
			loc = loc + value
		else:
			loc = loc + ", " + value
	print loc
	print "Rating: %d/5" %restaurant.rating
	decision = raw_input("Would you like to visit this restaurant? (Type y or n)")
	if(decision == 'y' or decision =='Y'):
		quit()
	elif(decision == 'n' or decision =='N'):
		print"\n"
		continue
	else:
		quit()
print "Please try a different search term"