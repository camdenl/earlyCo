__author__ = 'camden'

from geopy.geocoders import GoogleV3 as goog
from geojson import Feature, Point, FeatureCollection, loads, dumps
import os

def point_from_string(address):
    """
    geocode an address and get the latitude and longitude coordinates

    :param address: string representing address to geocode
    :return: array of [lat, long] coordinates
    """
    try:
        geoloc = goog()
        loc = geoloc.geocode(address)
        return [loc.latitude, loc.longitude]
    except Exception:
        return None


def create_feature(lat, lng, name, address, loc):
    """
    create a geojson feature given an address string and the loc of feature

    :param address: comma delimited string in form 'address, city, state zip, country'
    :param loc: string representing the data loc: 'dropbox, resource, sign'
    :return: geojson.feature object
    """

    if loc not in ['dropbox', 'resource', 'sign']:
        raise ValueError('invalid loc')

    properties = {
        'loc': loc,
        'name': name,
        'addr': address
    }

    f = Feature(geometry=Point([lng,lat]), properties=properties)
    return f


def create_geojson(feature):
    crs = {
    "type": "name",
    "properties": {
        "name": "EPSG:4326"
        }
    }

    try:
        if os.path.exists('static/features.json'):
            with open('static/features.json', 'r') as gj:
                feat_coll = gj.read()
            feat_coll = loads(feat_coll)
            feats = feat_coll.features
            feats.append(feature)
            with open('static/features.json', 'w') as gj:
                gj.write(dumps(feat_coll))
        else:
            with open('static/features.json', 'w') as gj:
                gj.write(dumps(FeatureCollection([feature], crs = crs)))
        return 'ok'
    except Exception:
        return 'error'
