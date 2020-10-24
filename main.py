import unittest
from protocol_analyzer import myFunc

class myTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual(myFunc(), 20)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()

