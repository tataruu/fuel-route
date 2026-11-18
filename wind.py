import math

def zero_wind(lat, lon):
    return (0.0,0.0)

def make_jet_stream(center_lat = 45.0, width_deg = 4.0, peak_ms = 60.0):
    def wind(lat , lon):
        u = peak_ms * math.exp(-((lat - center_lat) / width_deg) ** 2)
        return (u , 0.0)

    return wind

