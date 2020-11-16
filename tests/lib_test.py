# -*- coding: UTF-8 -*-

# Import from our lib
from data_anything.lib import haversine_went_nuts
import pytest


def test_haversine_went_nuts():
    assert haversine_went_nuts() < 1412
