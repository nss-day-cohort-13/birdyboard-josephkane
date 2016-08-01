import unittest

class TestCreateUser(unittest.TestCase):

	def test_new_user_is_user(self):
		test_user = User()
		self.assertIsInstance(test_user, User)