import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

import unittest
from starbucks_kmeans.kmeans import GraphPoint, KmeansPoint, determine_is_closer, reset_graph_point, refocus_kmeans_point

class Kmeans(unittest.TestCase):

    # reset_graph_point
    # -----------------
    def test_reset_graph_point(self):
        # Arrange
        graph_point = GraphPoint(location=[],name=None)
        graph_point.nearest_value_id = 10
        graph_point.nearest_value_distance = 2

        # Act
        reset_graph_point(graph_point=graph_point)

        # Assert
        self.assertTrue(graph_point.nearest_value_distance == float("inf"))
        self.assertTrue(graph_point.nearest_value_id == -1)
    
    # determine_is_closer 
    # -------------------
    def test_determine_is_closer_true(self):
        # Arrange
        graph_point = GraphPoint(location=[3,4],name=None)
        kmeans_point = KmeansPoint(location=[0,0],point_id=1)

        # Act
        determine_is_closer(kmeans_point=kmeans_point, graph_point=graph_point)

        # Assert
        self.assertTrue(graph_point.nearest_value_distance == 5)
        self.assertTrue(graph_point.nearest_value_id == 1)
    
    def test_determine_is_closer_false(self):
        # Arrange
        graph_point = GraphPoint(location=[3,4],name=None)
        graph_point.nearest_value_distance = 1
        graph_point.nearest_value_id = 2

        kmeans_point = KmeansPoint(location=[0,0],point_id=1)

        # Act
        determine_is_closer(kmeans_point=kmeans_point, graph_point=graph_point)

        # Assert
        self.assertTrue(graph_point.nearest_value_distance == 1)
        self.assertTrue(graph_point.nearest_value_id == 2)
    
    # refocus_kmeans_point
    # --------------------
    def test_refocus_kmeans_point_move(self):
        # Arrange
        graph_point = GraphPoint(location=[3,4],name=None)
        graph_point.nearest_value_id = 1

        kmeans_point = KmeansPoint(location=[0,0],point_id=1)

        # Act
        result = refocus_kmeans_point(kmeans_point=kmeans_point, graph_points=[graph_point])

        # Assert
        self.assertTrue(kmeans_point.location == [3,4])
        self.assertTrue(result)
    
    def test_refocus_kmeans_point_no_move(self):
        # Arrange
        graph_point = GraphPoint(location=[3,4],name=None)
        graph_point.nearest_value_id = 1

        kmeans_point = KmeansPoint(location=[3,4],point_id=1)

        # Act
        result = refocus_kmeans_point(kmeans_point=kmeans_point, graph_points=[graph_point])

        # Assert
        self.assertTrue(kmeans_point.location == [3,4])
        self.assertFalse(result)
    
    def test_refocus_kmeans_point_error(self):
        # Arrange
        graph_point = GraphPoint(location=[3,4],name=None)
        graph_point.nearest_value_id = 2

        kmeans_point = KmeansPoint(location=[0,0],point_id=1)

        result = False

        # Act
        try:
            _ = refocus_kmeans_point(kmeans_point=kmeans_point, graph_points=[graph_point])
        except ValueError:
            result = True

        # Assert
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()