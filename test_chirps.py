import unittest
from chirps import *
from random_id_generator import *

class TestChirp(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.public = Chirp("Hello!", "jkane", random_id_generator())
		self.private = Chirp("Hello!", "jkane", random_id_generator(), private=True, recipient="rtanay")

	def test_public_and_private_chirps_are_chirps(self):
		self.assertIsInstance(self.public, Chirp)
		self.assertIsInstance(self.private, Chirp)

	def test_public_chirp_creation(self):
		self.assertEqual(self.public.author, "jkane")
		self.assertEqual(self.public.message, "Hello!")
		self.assertEqual(self.public.private, False)

	def test_private_chirp_creation(self):
		self.assertEqual(self.private.author, "jkane")
		self.assertEqual(self.private.recipient, "rtanay")
		self.assertEqual(self.private.message, "Hello!")
		self.assertEqual(self.private.private, True)

if __name__ == "__main__":
	unittest.main()
