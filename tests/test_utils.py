import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

import unittest
from starbucks_kmeans.utils import list_pythag, list_calculate_mean

class Utils(unittest.TestCase):

    # list_pythag
    # -----------
    def test_list_pythag_2d(self):
        # Arrange
        point_a = [ 0, 0 ]
        point_b = [ 3, 4 ]

        # Act
        result = list_pythag(point_a=point_a, point_b=point_b)

        # Assert
        expected = 5
        self.assertTrue(expected == result)
    
    def test_list_pythag_5d(self):
        # Arrange
        point_a = [ 0, 0, 0, 0, 0 ]
        point_b = [ 3, 4, 4, 2, 2 ]

        # Act
        result = list_pythag(point_a=point_a, point_b=point_b)

        # Assert
        expected = 7
        self.assertTrue(expected == result)
    
    # list_calculate_mean
    # -------------------
    def test_list_calculate_mean_2(self):
         # Arrange
        lists = [ [ 0, 0, 1 ], [ 1, 0, 1 ] ]

        # Act
        result = list_calculate_mean(lists=lists)

        # Assert
        expected = [ .5, 0, 1 ]
        self.assertTrue(expected == result)
    
    def test_list_calculate_mean_4(self):
         # Arrange
        lists = [ [ 0, 0, 0, 1 ], [ 0, 0, 1, 1 ], [0, 1, 1, 1], [1, 1, 1, 1] ]

        # Act
        result = list_calculate_mean(lists=lists)

        # Assert
        expected = [ .25, .5, .75, 1 ]
        self.assertTrue(expected == result)

if __name__ == "__main__":
    unittest.main()