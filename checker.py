from PIL import Image
import numpy as np
from skimage.morphology import remove_small_objects


def time_detection(image, threshold=30):
    gray = np.array(image.convert('L'))
    return np.mean(gray) > threshold


def analyze(image, grid_size=(8, 6), day_threshold=200, night_threshold=50, min_size=10):
    gray = np.array(image.convert('L'))

    if time_detection(image):
        mask = (gray > day_threshold)
    else:
        mask = (gray < night_threshold)

    clean_mask = remove_small_objects(mask, min_size=min_size)
    cloud_pixel = np.sum(clean_mask)
    total_pixel = gray.size
    
    return (cloud_pixel / total_pixel) * 100
