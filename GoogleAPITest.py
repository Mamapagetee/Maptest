import pprint
import googlemaps


gmaps = googlemaps.Client('AIzaSyCe587EiY55OFSctTuapkQUD-tXf76pGro')

places_results = gmaps.places_nearby(location='21.4053206,-157.8074451', rank_by='distance', open_now=False, type='cafe')

for place in places_results['results']:

    my_place_id = place['place_id']

    my_fields = ['name', 'formatted_phone_number', 'type']

    place_details = gmaps.place(place_id = my_place_id)

    pprint.pprint(place_details)