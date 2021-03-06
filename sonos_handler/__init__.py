import soco
from soco.discovery import by_name

def setup_device(name):
	device = by_name(name)

	return device

def play_album(device, album):
	print(f"Playing {album} on {device}")

	print("Getting info")
	items = device.music_library.get_music_library_information(
		"albums", search_term=album, complete_result=True
	)

	if len(items) == 0:
		print("No album found")
	elif len(items) > 1:
		print("More than one item matched, not sure what to do")
	else:
		print(f"Found {items[0]}")

		print("Clearing the queue")
		#device.clear_queue()

		#print(device.add_to_queue(items[0], position=1))
