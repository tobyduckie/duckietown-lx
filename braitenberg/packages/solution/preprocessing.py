import cv2
import numpy as np

#lower_hsv = np.array([0, 130, 45])
#upper_hsv = np.array([90, 240, 255])
lower_hsv = np.array([0, 120, 180])
upper_hsv = np.array([90, 250, 255])
#lower_hsv = np.array([0, 0, 0])
#upper_hsv = np.array([110, 200, 255])


def preprocess(image_rgb: np.ndarray) -> np.ndarray:
    """Returns a 2D array"""
    hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    return mask
