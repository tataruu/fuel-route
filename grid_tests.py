import pytest
from grid import haversine_km

LHR = (51.47, -0.45)
JFK = (40.64, -73.78)

def test_some_point_is_zero():
    assert haversine_km(*LHR, *JFK) == pytest.approx(0.0, abs=1e-9)


def test_half_planet():
    assert haversine_km(0,0,0,180) == pytest.approx(20015.1, abs=1e-3)

def test_london_to_jfk():
    assert haversine_km(*LHR, *JFK) == pytest.approx(5540.5, abs=1e-3)

def test_distance_is_symmetric():
    assert haversine_km(*LHR, *JFK) == pytest.approx(haversine_km(*JFK, *LHR))
