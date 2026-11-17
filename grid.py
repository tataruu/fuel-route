import math

EARTH_RADIUS_KM = 6371.0

def haversine_km(lat1, lon1, lat2, lon2):

    lat1,lon1,lat2,lon2 = map(math.radians, (lat1, lon1, lat2, lon2))

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = math.sin(delta_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon/2)**2
    a = min(1.0, a)


    d = 2 * EARTH_RADIUS_KM * math.asin(math.sqrt(a))
    return d


def bearing_rad(lat1, lon1, lat2, lon2):
    lat1,lon1,lat2,lon2 = map(math.radians, (lat1, lon1, lat2, lon2))

    delta_lon = lon2-lon1
    y = math.sin(delta_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)

    return math.atan2(y, x)

def midpoint(lat1, lon1, lat2, lon2):
    return ((lat1 + lat2) / 2, (lon1 + lon2) / 2)


