import math
from dataclasses import dataclass

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




@dataclass(frozen=True)
class Grid:

    lat_min: float
    lat_max: float
    lon_min: float
    lon_max: float
    step:float = 1.0

    @property
    def n_rows(self):
        return int((round(self.lat_max - self.lat_min) / self.step)) + 1
    @property
    def n_cols(self):
        return int((round(self.lon_max - self.lon_min) / self.step)) + 1

    def coords(self, node):
        row, col = node
        lat = self.lat_min + row * self.step
        lon = self.lon_min + col * self.step
        return (lat, lon)

    def nearest_node(self , lat , lon ):
        row = int(round((lat - self.lat_min) / self.step))
        col = int(round((lon - self.lon_min) / self.step))

        return (row, col)

    def in_bounds(self, node):
        row, col = node
        return (row >= 0 and row < self.n_rows) and (col >= 0 and col < self.n_cols)


NORTH_ATLANTIC = Grid(lat_min = 30 , lat_max = 70 , lon_min= -85 , lon_max =30 , step = 1.0 )


AIRPORTS = {
    "LHR": (51.47, -0.45),
    "JFK": (40.64, -73.78),
    "CLJ": (46.79, 23.69),
}

