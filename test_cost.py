import math

import pytest

from cost import edge_time_hours
from grid import haversine_km
from wind import zero_wind

TAS = 250.0


def test_zero_wind_time_is_distance_over_airspeed():
    expected = haversine_km(50, -10, 50, -9) / (TAS * 3.6)
    assert edge_time_hours(50, -10, 50, -9, zero_wind, TAS) == pytest.approx(expected)

def east_50(lat, lon):
    return (50.0, 0.0)  # 50 m/s blowing east, everywhere

def test_tailwind_is_faster_headwind_is_slower():
    calm = edge_time_hours(50, -10, 50, -9, zero_wind, TAS)
    eastbound = edge_time_hours(50, -10, 50, -9, east_50, TAS)  # -10 → -9: flying east, wind behind you
    westbound = edge_time_hours(50, -9, 50, -10, east_50, TAS)  # -9 → -10: flying west, wind in your face
    assert eastbound < calm < westbound


def north_50(lat, lon):
    return(0.0, 50.0)

def test_crosswind_doesnt_affect():
    eastbound = edge_time_hours(0, 10, 0, 11, north_50, TAS)
    calm = edge_time_hours(0, 10, 0, 11, zero_wind, TAS)

    assert eastbound == pytest.approx(calm)


def east_300(lat, lon):
    return (300.0, 0.0)
def test_headwind_bigger_than_speed():
    time = edge_time_hours(50 , -9 , 50 , -10 , east_300, TAS)
    assert time == math.inf