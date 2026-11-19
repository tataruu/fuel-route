import math

from grid import haversine_km, bearing_rad, midpoint

MS_TO_KMH = 3.6

def edge_time_hours(lat1,lon1,lat2,lon2, wind, tas_ms):
    distance_km = haversine_km(lat1, lon1, lat2, lon2)
    heading = bearing_rad(lat1, lon1, lat2, lon2)
    mid = midpoint(lat1, lon1, lat2, lon2)
    u , v = wind(*mid)
    tail_wind = u * math.sin(heading) + v * math.cos(heading)


    ground_speed_ms = tas_ms + tail_wind
    if ground_speed_ms <= 0:
        return math.inf


    return distance_km / (ground_speed_ms * MS_TO_KMH)

