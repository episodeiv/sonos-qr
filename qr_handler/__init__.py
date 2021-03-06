import re
import time

valid_code = re.compile('^sonos-qr:([a-z0-9_ ]+)', re.IGNORECASE)
same_code_timeout = 10.0
previous_code = None


def handle_code(content):
	global previous_code
	if not is_valid(content):
		print("Read invalid code")
		return False

	if previous_code is not None and content == previous_code:
		print("Seen that before")
		time.sleep(same_code_timeout)
		return False

	match = re.search(valid_code, content)

	album = match.group(1)

	previous_code = content

	return album


def is_valid(content):
	if content is None:
		return False

	match = re.search(valid_code, content)

	if match:
		return True
	else:
		return False
