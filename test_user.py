import unittest
from user import *

class TestUser(unittest.TestCase):

	def test_new_user_is_user(self):
		test_user = User("jkane", "Joe")
		self.assertIsInstance(test_user, User)
		self.assertEqual(test_user.screen_name, "jkane")
		self.assertEqual(test_user.full_name, "Joe")

if __name__ == "__main__":
	unittest.main()