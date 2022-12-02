from .alvinxy import Transformer
import math


class WGS84TransformAlvinXY:
    """Transforms between WGS84 points and transverse mercator planes"""

    def __init__(self, crs_name, offset, origin):
        print(f'WGS84Transform({crs_name}, {offset})')
        self.crs_name = crs_name
        self.x = offset[0]
        self.y = offset[1]
        self.origin_lat = origin[0]
        self.origin_lon = origin[1]
        print(self.crs_name)
        self.rotation = 0
        self.wgs84_to_tm = \
            Transformer.from_crs("EPSG:4326", self.crs_name)

    def transform_point(self, p):
        lon = p[0]
        lat = p[1]
        (tm_northing, tm_easting) = \
            self.wgs84_to_tm.transform(lat, lon,  self.origin_lat, self.origin_lon )
        print(f'lat={lat} lon={lon} => ({tm_easting}, {tm_northing})')

        return (tm_easting, tm_northing)
    
