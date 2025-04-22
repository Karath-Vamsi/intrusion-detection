# utils.py

import cv2
import numpy as np

def is_point_inside_polygon(point, polygon):
    return cv2.pointPolygonTest(polygon, point, False) >= 0
