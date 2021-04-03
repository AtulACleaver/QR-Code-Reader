# Read image/ camera/ video input
import cv2
# This will decode the qr code.
from pyzbar.pyzbar import decode

img = cv2.imread('My Github Profile.png')
print(decode(img))

