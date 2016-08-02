import unittest
from user import *

class TestUser(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.user = User("Joe", "jkane", random_id_generator())

	def test_new_user_is_user(self):
		self.assertIsInstance(self.user, User)
		self.assertEqual(self.user.screen_name, "jkane")
		self.assertEqual(self.user.full_name, "Joe")

if __name__ == "__main__":
	unittest.main()