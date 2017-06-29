import subprocess
import unittest


class TestFindSecondLargestNumber(unittest.TestCase):
    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "find_second_largest_number.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_positive_numbers(self):
        actual_output = self.process.communicate(input='5\n2 3 6 5')[0]
        self.assertEquals('5\n', actual_output)

    def test_positive_numbers_with_multiple_max_occurances(self):
        actual_output = self.process.communicate(input='5\n2 3 6 6 5')[0]
        self.assertEquals('5\n', actual_output)

    def test_positive_and_negative_numbers(self):
        actual_output = self.process.communicate(input='5\n2 3 6 -6 5')[0]
        self.assertEquals('5\n', actual_output)

    def test_positive_and_negative_numbers_with_multiple_max_occurences(self):
        actual_output = self.process.communicate(input='5\n2 3 6 6 -6 5')[0]
        self.assertEquals('5\n', actual_output)

    def test_negative_numbers(self):
        actual_output = self.process.communicate(input='5\n-2 -3 -6 -6 -5')[0]
        self.assertEquals('-3\n', actual_output)

    def test_negative_numbers_with_multiple_occurences_of_max(self):
        actual_output = self.process.communicate(
            input='5\n-2 -2 -3 -6 -6 -5'
        )[0]

        self.assertEquals('-3\n', actual_output)

    '''
    test with multiple instances of max large
    '''


if __name__ == '__main__':
    unittest.main()
