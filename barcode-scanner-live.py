import cv2
from pyzbar import pyzbar
import imutils
from imutils.video import VideoStream
import time

from qr_handler import handle_code


print("Setting up video")

vs = VideoStream (usePiCamera = True).start()
time.sleep(2.0)

while True:
	print("Getting image")

	frame = vs.read()
	# scale down image
#    frame = imutils.resize(frame, width=400)
	frame = imutils.resize(frame, width=500, inter=cv2.INTER_NEAREST)

	barcodes = pyzbar.decode(frame)

	for barcode in barcodes:
		data = barcode.data.decode("utf-8")
		print(data)
		handle_code(data)
	time.sleep(0.5)
