import unittest
import random
import numpy as np
import sys
#sys.path.append('../')
import data_processor  # nopep8


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        """Create toy data for tests
        """
        array56 = a = np.empty((5,6))
        np.savetxt("test56.csv", array56, delimiter=",")
        cls.f56 = 'test56.csv'

    @classmethod
    def tearDownClass(cls):

        """Get rid of toy data created in setup
        """

    def test_get_random_matrix(cls):

        """Test that get_random_matrix functions correctly
        """

        # positive test: returns data of correct shape
        cls.assertEqual(np.shape(data_processor.get_random_matrix(2, 3)),
                        (2, 3))

        # negative test: does not return data of incorrect shape
        cls.assertNotEqual(np.shape(data_processor.get_random_matrix(2, 3)),
                           (3, 2))

        # check that correct errors are raised
        cls.assertRaises(TypeError,
                         data_processor.get_random_matrix,
                         'three',
                         3)
        cls.assertRaises(ValueError,
                         data_processor.get_random_matrix,
                         -2,
                         3)

    def test_get_file_dimensions(cls):

        """Test that get_file_dimensions functions correctly
        """
        
        # positive test: returns correct shape
        cls.assertEqual(data_processor.get_file_dimensions(cls.f56, False),
                        (5, 6))

        # negative test: does not return data of incorrect shape
        cls.assertNotEqual(data_processor.get_file_dimensions(cls.f56, False),
                          (6, 5))

        # check that correct errors are raised
        cls.assertRaises(ValueError,
                         data_processor.get_file_dimensions,
                         'csvDNE.csv',
                         has_header='No')
        cls.assertRaises(FileNotFoundError,
                         data_processor.get_file_dimensions,
                         'csvDNE.csv',
                         has_header=False)

    def test_write_matrix_to_file(cls):

        """Test that write_file_to_text functions correctly
        """
        
        # positive test: test that matrix created has the correct dimensions 
        data_processor.write_matrix_to_file(2,3, 'testfile.csv')
        true_dim = data_processor.get_file_dimensions('testfile.csv',
                                                      has_header=False)
        cls.assertEqual(true_dim, (2,3))

        # negative test: 
        cls.assertNotEqual(true_dim, (3,2))

        # check that correct errors are raised
        cls.assertRaises(TypeError,
                         data_processor.write_matrix_to_file,
                         'three',
                         3,
                         'file.csv')
        cls.assertRaises(ValueError,
                         data_processor.write_matrix_to_file,
                         -2,
                         3,
                         'file.csv')
        cls.assertRaises(NameError,
                         data_processor.write_matrix_to_file,
                         2,
                         3,
                         2)

if __name__ == '__main__':
    unittest.main()