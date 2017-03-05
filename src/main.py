"""
person finder

* take pictures from ftp folder /new
* try to find person in jpg
* if found -> alert
* else drop

author: oliver moser, https://twitter.com/moseroli

"""

from config import *
import cv2
import os
import glob
import shutil
import detectors


def prepare_paths():
    """
    create test folder structure
    """
    for d in DIRS:
        directory = os.path.dirname(d)
        try:
            os.stat(directory)
        except FileNotFoundError:
            logger.debug("dir not found. creating {0}".format(directory))
            os.mkdir(directory)


def process_file(f):
    file_name = f.split("/")[-1]
    logger.debug("processing: {0}".format(file_name))
    shutil.move(f, PATH_PROCESS)

    image = cv2.imread(PATH_PROCESS + file_name)
    rois = detectors.detect_person(image)

    logger.info("found {0} persons".format(len(rois)))

    if DEBUG:
        cv2.drawContours(image, rois, -1, ROI_COLOR)
        cv2.imshow("image", image)
        cv2.waitKey(0)


def find_new_pictures():
    file_list = glob.glob(PATH_NEW_IMAGES + FILE_PATTERN)

    if len(file_list) == 0:
        logger.debug("no new files. nothing to do. ...")
        return

    for f in file_list:
        process_file(f)


prepare_paths()
find_new_pictures()

cv2.destroyAllWindows()
