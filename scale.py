def scope(geo_object):
    envelope = geo_object["boundedBy"]["Envelope"]
    lower_corner = list(map(float, envelope["lowerCorner"].split()))
    upper_corner = list(map(float, envelope["upperCorner"].split()))

    _delta_x = (upper_corner[0] - lower_corner[0]) * 0.5
    _delta_y = (upper_corner[1] - lower_corner[1]) * 0.5

    return _delta_x, _delta_y
