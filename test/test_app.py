from app.multi import multiplicacion
import unittest

class TestMulti(unittest.TestCase):
	def test_multi(self):
		self.assertEqual(multiplicacion(2,3),6)

if __name__ == '__main__':
	unittest.main()
