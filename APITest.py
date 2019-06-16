import json
import urllib.parse

'''
this function could really easily be used with any api and data set.
I'm currently working on making the operations more universal.
'''


# test function for retrieving data
def property_details_test_function(address=None, city=None, state=None, resourse='avm', package='detail'):

    # api specific parameters for retrieval
    url_base = 'https://api.gateway.attomdata.com/propertyapi/v1.0.0/'
    headers = {'accept': 'application/json',
               'apikey': '5bdc80b8721e3e3139bfad45c7f70c60'}

    # url generator from parameters
    address1 = address
    address2 = city + ' ' + state
    url = url_base + resourse + '/' + package + '?' + 'address1=' + urllib.parse.quote(address1) + '&' + 'address2=' + urllib.parse.quote(address2)

    # url retriever
    response = requests.get(url=url, headers=headers)

    # url retrieval status
    if response.status_code == 200:
        print('SuccessfulWithUrl')
        json.loads(response.content.decode('utf-8'))

        # json parser
        home_data = requests.get(url=url, headers=headers).json()
        # json file status message
        status_data = home_data['status']['msg']
        print(status_data)

        # data path
        latitude_data = home_data['property'][0]['location']['latitude']
        longitude_data = home_data['property'][0]['location']['longitude']
        home_type_data = home_data['property'][0]['summary']['propsubtype']
        beds_data = home_data['property'][0]['building']['rooms']['beds']
        baths_data = home_data['property'][0]['building']['rooms']['bathstotal']
        condition_data = home_data['property'][0]['building']['construction']['condition']

        # output
        print('latitude: ' + latitude_data)
        print('longitude: ' + longitude_data)
        print('home type: ' + home_type_data)
        print('beds: ' + str(beds_data))
        print('baths: ' + str(baths_data).strip('.0'))
        print('condition: ' + condition_data)
    else:
        print('ERROR 404: URL does not exist')


# function input
property_details_test_function('45-840 Anoi Road', 'Kaneohe', 'HI')

'''
function parameters: street address, city, state

I believe any address in america should work with this 
current api, but I have not completely tested it

Current Output:
    latitude: float
    longitude: float
    home type: type
    beds: int
    baths: int
    condition: condition
'''
