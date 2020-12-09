"""This unittest checks if the function 'covid' function works
UnitTests(unittest.TestCase) -- framework for functions testing
                                Exports 'OK', 'FAIL',
                                or 'ERROR'
def test_smoke(self) -- does function run-through w/o problems
"""


import unittest

import covid


class UnitTests(unittest.TestCase):
    """
    Testing the travis

    """

    def test_smoke(self):
        """
        Testing the travis

        """

        not_important = 3

        self.assertEqual(covid.test(not_important), 3)


if __name__ == '__main__':
    unittest.main()
