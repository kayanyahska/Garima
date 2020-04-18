import json
from urllib2 import urlopen
from Website.utilities.main import weightReturner

def routeFinder(originVal,destinationVal):
    originVal = originVal.replace(" ","+")
    destinationVal = destinationVal.replace(" ","+")
    #mapsURL = "" % (originVal,destinationVal)
    response = urlopen(mapsURL)
    data = json.loads(response.read().decode('utf-8'))
    coordinate_list = []
    number_routes = len(data.get('routes'))
    x = 0
    for route in data.get('routes'):
        coordinate_list.append([])
        for step in (route.get('legs')[0].get('steps')):
            lat = step.get('start_location').get('lat')
            lon = step.get('start_location').get('lng')
            coordinate_list[x].append((lat,lon))
        x+=1

    import datetime
    now = datetime.datetime.now()

    weighted_values_list = []
    x = 0
    for route in coordinate_list:
        weighted_values_list.append([])
        y = 0
        for step in route:
            weighted_values_list[x].append(weightReturner(str(coordinate_list[x][y][0]), str(coordinate_list[x][y][1]), now.hour))
            y+=1
        x+=1

    x = 0
    minimum = float(999999999)
    min_route = 0
    for route in weighted_values_list:
        if minimum > (float(sum(route))/len(route)):
            minimum = sum(route)/len(route)
            min_route = x
        x+=1

    return coordinate_list[min_route]



