import cv2
from pyzbar import pyzbar
import imutils
from imutils.video import VideoStream
import time

print("Setting up video")

vs = VideoStream (usePiCamera = True).start()
time.sleep(2.0)

while True:
    frame = vs.read()
    # scale down image
    frame = imutils.resize(frame, width=400)

    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        print(barcode.data.decode("utf-8"))
