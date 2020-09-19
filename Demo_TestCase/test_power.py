import unittest
import power

class TestPower(unittest.TestCase):

	def test_power_integer(self):
		num1= 5
		num2 = 2
		result = power.pow(num1,num2)
		self.assertEqual(result,25)

	def test_power_decimal(self):
		num1= 25.0
		num2 = 2
		result = power.pow(num1,num2)
		self.assertEqual(result, 625)

if __name__ =='__main__':
	unittest.main()
