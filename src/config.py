"""
config file

author: oliver moser, https://twitter.com/moseroli
"""

import logging.config
from os import path

logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logging.conf'))
logger = logging.getLogger('myLogger')


BASE_PATH = "../ftp-test/"

PATH_NEW_IMAGES = BASE_PATH + "new/"
PATH_PROCESS = BASE_PATH + "process/"
PATH_PROCESSED = BASE_PATH + "processed/"
PATH_ALERT = BASE_PATH + "alert/"

DIRS = [BASE_PATH, PATH_NEW_IMAGES, PATH_PROCESS, PATH_PROCESSED, PATH_ALERT]

IMAGE_PATTERN = "*.jpg"
VIDEO_PATTERN = "*.avi"
ROI_COLOR = (0, 255, 0)

DEBUG = True
