import unittest
from random_id_generator import *
from user import *

class TestRandomID(unittest.TestCase):

	def test_random_id_generator_is_an_int(self):
		self.user = User("Joe", "jkane", random_id_generator())
		self.assertIsInstance(self.user.user_id, int)
		self.assertEqual(len(str(self.user.user_id)), 5)

if __name__ == "__main__":
	unittest.main()