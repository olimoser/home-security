from config import *
import cv2

body_cascade = cv2.CascadeClassifier('./detectors/haarcascade_upperbody.xml')


def detect_person(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rois = body_cascade.detectMultiScale(gray, 2.5, 2)
    return rois

