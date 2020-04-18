import gmplot
from Website.utilities.start import routeFinder

def findPath(originVal, destinationVal):
	my_list = routeFinder(originVal,destinationVal)
	lonList = []
	latList = []
	for (x,y) in my_list:
	    latList.append(x)
	    lonList.append(y)
	gmap = gmplot.GoogleMapPlotter(39.952583,-75.165222,13)
	gmap.scatter( latList, lonList, '# FF0000', size = 40, marker = False )
	gmap.plot(latList, lonList,  'cornflowerblue', edge_width = 2.5)
	gmap.draw( "/home/akshay/alpha/Website/templates/map.html" )  

	return gmap
