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


def process_image(f):
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


def process_video(f):
    file_name = f.split("/")[-1]
    logger.debug("processing: {0}".format(file_name))
    shutil.move(f, PATH_PROCESS)

    video = cv2.VideoCapture(PATH_PROCESS + file_name)

    while video.isOpened():
        ret, frame = video.read()
        #rois = detectors.detect_person(frame)
        #logger.info("found {0} persons".format(len(rois)))

        if DEBUG:
            #cv2.drawContours(frame, rois, -1, ROI_COLOR)
            cv2.imshow("image", frame)
            cv2.waitKey(1)


def find_new_pictures():
    file_list = glob.glob(PATH_NEW_IMAGES + IMAGE_PATTERN)

    if len(file_list) == 0:
        logger.debug("no new images. nothing to do. ...")
        return

    for f in file_list:
        process_image(f)


def find_new_videos():
    file_list = glob.glob(PATH_NEW_IMAGES + VIDEO_PATTERN)

    if len(file_list) == 0:
        logger.debug("no new videos. nothing to do. ...")
        return

    for f in file_list:
        process_video(f)


prepare_paths()
find_new_pictures()

find_new_videos()

cv2.destroyAllWindows()
