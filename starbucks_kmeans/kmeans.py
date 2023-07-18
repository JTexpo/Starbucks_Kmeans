from typing import List, Optional

from starbucks_kmeans.utils import list_pythag, list_calculate_mean


class GraphPoint:
    def __init__(self, location: List[float], name: Optional[str] = None):
        self.location = location
        self.nearest_value_id = -1
        self.nearest_value_distance = float("inf")
        self.name = name


class KmeansPoint:
    def __init__(self, location: List[float], point_id: int):
        self.location = location
        self.point_id = point_id


"""
GraphPoint
----------
"""
def determine_is_closer(kmeans_point: KmeansPoint, graph_point: GraphPoint) -> None:
    """A function to update a graph point if its distance to a kmeans point is less than it's current nearest point

    Args:
        kmeans_point (KmeansPoint): a cluster centroid
        graph_point (GraphPoint): a data point on our graph
    """
    # Calculate the distance
    distance = list_pythag(point_a=kmeans_point.location, point_b=graph_point.location)
    # If the distance is closer, than we want to update the graph point to reference this centroid
    if distance < graph_point.nearest_value_distance:
        graph_point.nearest_value_id = kmeans_point.point_id
        graph_point.nearest_value_distance = distance


def reset_graph_point(graph_point: GraphPoint) -> None:
    """A function to reset the IDs on the graph points

    Args:
        graph_point (GraphPoint): a data point on our graph
    """
    graph_point.nearest_value_id = -1
    graph_point.nearest_value_distance = float("inf")


"""
KmeansPoint
-----------
"""
def refocus_kmeans_point(
    kmeans_point: KmeansPoint, graph_points: List[GraphPoint]
) -> bool:
    """A function to shift all of the kmeans points

    Args:
        kmeans_point (KmeansPoint): a cluster centroid
        graph_points (List[GraphPoint]): All of the points on our graph

    Raises:
        ValueError: issolated kmeans, and to re-evaluate data

    Returns:
        bool: if the kmeans point shifted or not
    """
    # grabbing all of the ids that are close to our cluster
    id_graph_points = [
        graph_point.location
        for graph_point in graph_points
        if graph_point.nearest_value_id == kmeans_point.point_id
    ]
    # finding the new location for our kmeans cluster centroid
    new_location = list_calculate_mean(lists=id_graph_points)
    # if there is no location, then we raise an error to re-evaluate our data
    if not new_location:
        raise ValueError(f"kmeans point isolated at: {kmeans_point.location}\nPlease redefine kmeans locations or remove from pool.")
    # if there is no change in location, we return false
    if new_location == kmeans_point.location:
        return False
    # if there is a change in location, we return true and update our kmeans point
    kmeans_point.location = new_location
    return True


"""
Kmeans Algorithm
----------------
"""
def kmeans(kmeans_points: List[KmeansPoint], graph_points: List[GraphPoint]) -> None:
    """A function to preform Kmeans

    Args:
        kmeans_points (List[KmeansPoint]): A list of all of our kmeans centroids
        graph_points (List[GraphPoint]): A list of all of our data points on the graph
    """

    # 100 itterations should be enough to find the kmeans, if it doesn't exit early
    for _ in range(100):
        # finding nearest Kmeans point
        for kmeans_point in kmeans_points:
            for graph_point in graph_points:
                determine_is_closer(kmeans_point=kmeans_point, graph_point=graph_point)
        # updating all kmeans point to be in the center
        kmeans_updated = False
        for kmeans_point in kmeans_points:
            did_update = refocus_kmeans_point(
                kmeans_point=kmeans_point, graph_points=graph_points
            )
            if did_update:
                kmeans_updated = True
        # if kmeans did not update, then we have found the clasified spots
        if not kmeans_updated:
            return
        # restting all of the graphs to preform the opperation again
        for graph_point in graph_points:
            reset_graph_point(graph_point=graph_point)
