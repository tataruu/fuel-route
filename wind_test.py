import math

import pytest

from wind import make_jet_stream, zero_wind

def test_zero_wind():
    assert zero_wind(0, 0) == (0.0, 0.0)

def test_wind_is_strongest_at_center():
    jet = make_jet_stream()
    u,v = jet(45, -30)
    assert u == pytest.approx(60)


def test_wind_is_the_same_north_and_south():
    jet = make_jet_stream()
    north , _ = jet(48, 30) #3 degrees north
    south, _ = jet(42, 30) #3 degrees south
    assert north == pytest.approx(south)


def test_jet_fades():
    jet = make_jet_stream()
    u,_ = jet(65, 30)
    assert u < 0.01

def test_jet_with_different_parameters():
    jet = make_jet_stream(center_lat = 55.0, width_deg = 4.0, peak_ms = 60.0)
    u,v = jet(55, 30)
    assert u == pytest.approx(60)


def test_one_width_away_is_peak_times_e_minus_one():
    jet = make_jet_stream()
    u, _ = jet(49, 30)
    assert u == pytest.approx(60 * math.exp(-1))