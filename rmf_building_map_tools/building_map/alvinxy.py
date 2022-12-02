from math import *
import numpy as np

def mdeglat(lat):
    '''
    Provides meters-per-degree latitude at a given latitude
    
    Args:
    lat (float): latitude
    Returns:
    float: meters-per-degree value
    '''
    latrad = lat*2.0*pi/360.0

    dy = 111132.09 - 566.05 * cos(2.0*latrad) \
        + 1.20 * cos(4.0*latrad) \
        - 0.002 * cos(6.0*latrad)
    return dy

def mdeglon(lat):
    '''
    Provides meters-per-degree longitude at a given latitude
    Args:
    lat (float): latitude in decimal degrees
    Returns:
    float: meters per degree longitude
    '''
    latrad = lat*2.0*pi/360.0 
    dx = 111415.13 * cos(latrad) \
        - 94.55 * cos(3.0*latrad) \
    + 0.12 * cos(5.0*latrad)
    return dx


class TransformerLLtoXY():
    @staticmethod
    def transform( lat, lon, lat_origin, long_origin):
        '''
        AlvinXY: Lat/Long to X/Y
        Converts Lat/Lon (WGS84) to Alvin XYs using a Mercator projection.
        Args:
        lat (float): Latitude of location
        lon (float): Longitude of location
        orglat (float): Latitude of origin location
        orglon (float): Longitude of origin location
        Returns:
        tuple: (x,y) where...
            x is Easting in m (Alvin local grid)
            y is Northing in m (Alvin local grid)
        '''
        # print("AlvinXY: Lat/Long to X/Y")
        x = (lon - long_origin) * mdeglon(lat_origin)
        y = (lat - lat_origin) * mdeglat(lat_origin)
        return (x,y)


class TransformerXYtoLL():
    # def __init__(self, lat_origin, long_origin):
    #     self.lat_origin = lat_origin
    #     self.long_origin = long_origin
    @staticmethod
    def transform(x, y, lat_origin, long_origin):
        '''
        X/Y to Lat/Lon
        Converts Alvin XYs to Lat/Lon (WGS84) using a Mercator projection.
        Args:
        x (float): Easting in m (Alvin local grid)
        x (float): Northing in m (Alvin local grid)
        orglat (float): Latitude of origin location
        orglon (float): Longitude of origin location
        Returns:
        tuple: (lat,lon) 
        '''
        # print("AlvinXY: X/Y to Lat/Lon")
        lon = x/mdeglon(lat_origin) + long_origin
        lat = y/mdeglat(lat_origin) + lat_origin

        return (lat, lon)

class Transformer():

    
    @staticmethod
    def from_crs(source_crs, target_crs):
        if source_crs== "WGS84" or source_crs== "EPSG:4326" and target_crs=="UTM":
            xyt = TransformerLLtoXY()
            return xyt

        if source_crs== "UTM" and target_crs=="WGS84" or target_crs== "EPSG:4326":
            llt = TransformerXYtoLL()
            return llt
        
# Vectorize
# vxy2ll = np.vectorize(xy2ll)
# vll2xy = np.vectorize(ll2xy)