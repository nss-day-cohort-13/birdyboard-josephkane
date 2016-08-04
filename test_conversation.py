import unittest
from conversation import *
from random_id_generator import *

class TestConvo(unittest.TestCase):

	def test_convo_is_a_conversation(self):
		convo = Conversation(random_id_generator(), 1234567)
		self.assertIsInstance(convo, Conversation)