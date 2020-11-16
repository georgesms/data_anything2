# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>

from data_anything.computedist import haversine
import numpy as np

def haversine_went_nuts():
    a = np.random.randint(1,10,4)
    return haversine(*a)


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    print(haversine_went_nuts())
