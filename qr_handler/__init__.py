import re
import time

valid_code = re.compile('^sonos-qr:')
same_code_timoeut = 1.0
previous_code = None


def handle_code(content):
	if not is_valid(content):
		return False

	if(content == previous_code):
		time.sleep(same_code_timoeut)
		return False




def is_valid(content):
	if content is None:
		return False

	if valid_code.match(content):
		return True
	else:
		return False
