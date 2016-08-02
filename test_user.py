import unittest
from user import *

class TestUser(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.user = User("Joe", "jkane")

	def test_new_user_is_user(self):
		self.assertIsInstance(self.user, User)
		self.assertEqual(self.user.screen_name, "jkane")
		self.assertEqual(self.user.full_name, "Joe")

	def test_random_id_generator_is_an_int(self):
		self.assertIsInstance(self.user.user_id, int)
		self.assertEqual(len(str(self.user.user_id)), 5)

if __name__ == "__main__":
	unittest.main()