import soco
from soco.discovery import by_name

def setup_device(name):
	device = by_name(name)

	return device

def play_favorite(device, favorite):
	print(f"Playing {favorite} on {device}")
