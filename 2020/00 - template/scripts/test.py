import unittest
import script

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(script.func(), None)  # add assertion here


if __name__ == '__main__':
    unittest.main()
