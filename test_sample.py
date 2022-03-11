import unittest

from sample import add_two, add_three

class TestFuncs(unittest.TestCase):
  
  def test_add_two(self):
    self.assertEqual(add_two(1), 3)
    self.assertEqual(add_two(0), 2)
    self.assertEqual(add_two(3), 5)
    
  def test_add_three(self): 
    self.assertEqual(add_three(-2), 1)
    self.assertEqual(add_three(0), 3)
    self.assertEqual(add_three(3), 6)

if __name__ == '__main__':
  unittest.main()
