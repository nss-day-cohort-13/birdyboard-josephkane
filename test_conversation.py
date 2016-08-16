import unittest
from conversation import *
from random_id_generator import *

class TestConvo(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.public_convo = PublicConvo([735284, 937352, 573519], 746342)
		self.private_convo = PrivateConvo([735284, 937352, 573519], 735953)

	def test_convo_is_a_conversation(self):
		self.assertIsInstance(self.public_convo, Conversation)
		self.assertIsInstance(self.private_convo, Conversation)

	def test_public_convo_values(self):
		self.assertEqual(self.public_convo.permission, "public")
		self.assertEqual(self.public_convo.chirp_list, [735284, 937352, 573519])

	def test_private_convo_values(self):
		self.assertEqual(self.private_convo.permission, "private")
		self.assertEqual(self.private_convo.chirp_list, [735284, 937352, 573519])

if __name__ == "__main__":
	unittest.main()
