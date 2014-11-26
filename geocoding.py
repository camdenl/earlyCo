__author__ = 'camden'

from geopy.geocoder import GoogleV3 as goog
import geojson

def point_from_string(address):
    """
    geocode an address and get the latitude and longitude coordinates

    :param address: string representing address to geocode
    :return: array of [lat, long] coordinates
    """
    geoloc = goog()
    loc = geoloc.geocode(address)
    try
