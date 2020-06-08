import unittest

from qr_handler import is_valid

class TestValidation(unittest.TestCase):
	def test_valid_codes(self):
		"""
		Test some valid qr codes
		"""
		codes = [
			"sonos-qr:abcdef&token",
			"sonos-qr:1_2_3&t_o_k_e_n",
		]

		for code in codes:
			result = is_valid(code)
			self.assertTrue(result)

	def test_invalid_codes(self):
		"""
		Test some invalid qr codes
		"""
		codes = [
			"",
			None,
			"sonos-qr:abcdef",
			"some-prefix:abcdef"
		]

		for code in codes:
			result = is_valid(code)
			self.assertFalse(result)


if __name__ == '__main__':
	unittest.main()
