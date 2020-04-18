from urllib2 import urlopen
import json
import numpy as np

def weightReturner(latitude, longitude, hour):
    url = "https://data.phila.gov/resource/sspu-uyfa.json?$$app_token=bF12rIkELtbJ8PXnuzuZTWmVF"
    radius = "200"
    locationURL = url + ("&$where=within_circle(shape,%s,%s,%s)" % (latitude, longitude, radius))
    response = urlopen(locationURL)
    data = json.loads(response.read().decode('utf-8'))
    num_100 = 0
    num_200 = 0
    num_300 = 0
    num_400 = 0
    num_500 = 0
    num_600 = 0
    num_other = 0

    rdata = []
    labels = []

    for d in data:
        ucr = d.get("ucr_general")
        if ucr != "":
            ucr = int(ucr)
            ucr = ucr - (ucr % 100)
            if not (ucr == 700 or ucr == 1000 or ucr == 1100 or ucr == 1200 or ucr == 1300 or ucr ==1500 or (ucr > 1500 and ucr <= 2400) or ucr == 2600):
				if ucr == 100:
					num_100 += 1
				elif ucr == 200:
					num_200 += 1
				elif ucr == 300:
					num_300 += 1
				elif ucr == 400:
					num_400 += 1
				elif ucr == 500:
					num_500 += 1
				elif ucr == 600:
					num_600 += 1
				else:
					num_other += 1
				rdata.append((int(d.get('hour_'))))
				labels.append(ucr)

    print "Number of homicides = " + str(num_100)
    print "Number of rapes = " + str(num_200)
    print "Number of robberies = " + str(num_300)
    print "Number of assaults = " + str(num_400)
    print "Number of burglaries = " + str(num_500)
    print "Number of thefts = " + str(num_600)
    print "Number of other crimes = " + str(num_other)
    
    rnum_100 = 0
    rnum_200 = 0
    rnum_300 = 0
    rnum_400 = 0
    rnum_500 = 0
    rnum_600 = 0
    rnum_other = 0
    lenrdata = len(rdata)
    for i in range(lenrdata):
        if rdata[i] == hour:
            if labels[i] == 100:
                rnum_100 += 1
            elif labels[i] == 200:
                rnum_200 += 1
            elif labels[i] == 300:
                rnum_300 += 1
            elif labels[i] == 400:
                rnum_400 += 1  
            elif labels[i] == 500:
                rnum_500 += 1   
            elif labels[i] == 600:
                rnum_600 += 1   
            else:
                rnum_other += 1
    my_list = [rnum_100,rnum_200,rnum_300,rnum_400,rnum_500,rnum_600,rnum_other]
    max = my_list[0]
    x=0
    y=0
    for i in my_list:
        x += 1
        if i > max:
            max = i
            y=x
    crime = (100*y) if y!=7 else 'others'
    print str(crime) + " is most likely to happen at " + str(hour) + " hour"
    weightedNumber = (rnum_100*7 + rnum_200*6 + rnum_300*5 + rnum_400*4 + rnum_500*3 + rnum_600*2 + rnum_other*1)
    print "The weighted average number of crimes reported = " + str(weightedNumber)

    return weightedNumber





