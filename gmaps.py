import googlemaps

api_key = "xxxmy_private_keyxxx"

gmaps = googlemaps.Client(key=api_key)

address = gmaps.geocode("xxxsome_addressxxx")

for item in address:
	print("\n\\n\n")
	print(item)

