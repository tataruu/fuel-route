import math

import pytest

from grid import AIRPORTS, NORTH_ATLANTIC, Grid, bearing_rad, haversine_km, midpoint

LHR = (51.47, -0.45)
JFK = (40.64, -73.78)


# ---------- haversine_km ----------

def test_same_point_is_zero():
    assert haversine_km(*LHR, *LHR) == pytest.approx(0.0, abs=1e-9)


def test_one_degree_on_equator():
    assert haversine_km(0, 0, 0, 1) == pytest.approx(111.195, rel=1e-3)


def test_half_planet():
    assert haversine_km(0, 0, 0, 180) == pytest.approx(20015.1, rel=1e-3)


def test_london_to_jfk():
    assert haversine_km(*LHR, *JFK) == pytest.approx(5540.5, rel=1e-3)


def test_distance_is_symmetric():
    assert haversine_km(*LHR, *JFK) == pytest.approx(haversine_km(*JFK, *LHR))


# ---------- bearing_rad ----------

def test_bearing_north():
    assert bearing_rad(0, 0, 1, 0) == pytest.approx(0.0, abs=1e-6)


def test_bearing_east():
    assert bearing_rad(0, 0, 0, 1) == pytest.approx(math.pi / 2, abs=1e-6)


def test_bearing_west():
    assert bearing_rad(0, 0, 0, -1) == pytest.approx(-math.pi / 2, abs=1e-6)


def test_bearing_south():
    # south is pi or -pi depending on rounding, so compare the absolute value
    assert abs(bearing_rad(0, 0, -1, 0)) == pytest.approx(math.pi, abs=1e-6)


def test_bearing_london_to_jfk():
    assert math.degrees(bearing_rad(*LHR, *JFK)) == pytest.approx(-72.05, abs=0.01)


def test_bearing_jfk_to_london():
    assert math.degrees(bearing_rad(*JFK, *LHR)) == pytest.approx(51.35, abs=0.01)


# ---------- midpoint ----------

def test_midpoint():
    assert midpoint(0, 0, 10, 20) == pytest.approx((5, 10))

#-----------grid class ---------

G = NORTH_ATLANTIC

def test_grid_size():
    assert(G.n_rows , G.n_cols ) == (41, 116)

def test_coords_of_corners():
    assert G.coords((0, 0)) == pytest.approx((30.0, -85.0))
    assert G.coords((40, 115)) == pytest.approx((70.0, 30.0))


def test_nearest_node_of_airports():
    assert G.nearest_node(*AIRPORTS["LHR"]) == (21, 85)
    assert G.nearest_node(*AIRPORTS["JFK"]) == (11, 11)


def test_nearest_node_returns_ints():
    row, col = G.nearest_node(*AIRPORTS["LHR"])
    assert isinstance(row, int) and isinstance(col, int)


def test_in_bounds():
    assert G.in_bounds((0, 0))
    assert G.in_bounds((40, 115))
    assert not G.in_bounds((41, 0))
    assert not G.in_bounds((0, 116))
    assert not G.in_bounds((-1, 0))
    assert not G.in_bounds((0, -1))
