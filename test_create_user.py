import unittest
from user import *

class TestUser(unittest.TestCase):

	def test_new_user_is_user(self):
		test_user = User()
		self.assertIsInstance(test_user, User)

	def test_create_new_user(self):
		test_user = User()
		test_user.screen_name = "jkane"
		test_user.full_name = "Joe"
		new_user = User()
		new_user = new_user.create_new_user("jkane", "Joe")
		self.assertEqual(test_user.screen_name, new_user.screen_name)
		self.assertEqual(test_user.full_name, new_user.full_name)

if __name__ == "__main__":
	unittest.main()