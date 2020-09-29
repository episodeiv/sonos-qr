import argparse
import cv2
from pyzbar import pyzbar
import imutils
from imutils.video import VideoStream
import time
import pprint

from qr_handler import handle_code
import sonos_handler

parser = argparse.ArgumentParser(description='Read QR codes and play favorites on Sonos speakers.')
parser.add_argument('--speaker', help='Name of the speaker to play to')
args = parser.parse_args()

print("Finding speaker")
device = sonos_handler.setup_device(args.speaker)

if device is None:
	print(f"Couldn't find speaker named {args.speaker}")
	exit()
print("Found device!")

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
		favorite = handle_code(data)
		sonos_handler.play_favorite(device, favorite)
	time.sleep(1)
