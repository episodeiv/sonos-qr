import re
import requests
import time

valid_code = re.compile('^sonos-qr:([a-z0-9_]+)&([a-z0-9_]+)', re.IGNORECASE)
same_code_timeout = 1.0
previous_code = None


def handle_code(content):
	global previous_code
	if not is_valid(content):
		return False

	if previous_code is not None and content == previous_code:
		print("Seen that before")
		time.sleep(same_code_timeout)
		return False

	match = re.search(valid_code, content)

	action = match.group(1)
	token = match.group(2)

	result = make_request(action, token)

	previous_code = content

	return result



def make_request(action, token):
	r = requests.get("https://maker.ifttt.com/trigger/" + action + "/with/key/" + token)

	if r.status_code == 200:
		return True
	else:
		return False



def is_valid(content):
	if content is None:
		return False

	match = re.search(valid_code, content)

	if match:
		return True
	else:
		return False
