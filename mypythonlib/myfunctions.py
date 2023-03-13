""""
Haversine formula is defined as follows
$a = sin^2(dLat/2) + cos(lat1) * cos(lat2) * sin^2(dLon/2)$
$c = 2 * atan2( √a, √(1−a) )$
$d = R * c$

Where:

    d is the distance between the two points in kilometers
    R is the radius of the Earth (mean radius = 6,371km)
    lat1 and lat2 are the latitude of point 1 and point 2, respectively, in radians
    dLat is the difference in latitude between the two points in radians
    dLon is the difference in longitude between the two points in radians

"""

#python code for Haversine formula

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r
