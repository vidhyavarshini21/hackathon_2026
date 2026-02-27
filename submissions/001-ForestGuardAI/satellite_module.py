import cv2
import numpy as np

def detect_deforestation(before_img, after_img):
    before = cv2.imread(before_img)
    after = cv2.imread(after_img)

    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(before_gray, after_gray)
    change_percent = np.sum(diff > 25) / diff.size * 100

    print(f"🛰 Forest Change Detected: {change_percent:.2f}%")

    return change_percent > 10
