import unittest
import random
import numpy as np
import sys
sys.path.append('../')
import data_processor  # nopep8


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        """Create toy data for tests
        """
        array_5_6 = a = np.empty((5,6))
        np.savetxt("test56.csv", array_5_6, delimiter=",")
        cls.testfile_5_6 = 'test56.csv'

    @classmethod
    def tearDownClass(cls):

        """Get rid of toy data created in setup
        """

    def test_get_random_matrix(cls):

        """Test that get_random_matrix functions correctly
        """

        # positive test: returns data of correct shape
        cls.assertEqual(np.shape(data_processor.get_random_matrix(2, 3)), (2, 3))

        # negative test: does not return data of incorrect shape
        cls.assertNotEqual(np.shape(data_processor.get_random_matrix(2, 3)), (3, 2))

if __name__ == '__main__':
    unittest.main()