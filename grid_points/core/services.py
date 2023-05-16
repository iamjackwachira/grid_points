import math


def find_closest_points(points: str) -> str:
    """Calculates the points that are closest to each other and returns it

    Args:
        points (str): String of semicolon separated coordinates

    Returns:
        str: String of semicolon separated coordinates
    """
    points_list = points.split(";")
    closest_points = ("", "")
    min_distance = float("inf")
    for i, point1 in enumerate(points_list[:-1]):
        x1, y1 = map(float, point1.split(","))
        for point2 in points_list[i + 1 :]:
            x2, y2 = map(float, point2.split(","))
            # Calculate the Euclidean distance and compare with the minimimum distance so far
            # https://www.cuemath.com/euclidean-distance-formula/
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if distance < min_distance:
                closest_points = (point1, point2)
                min_distance = distance
    return ";".join(closest_points)
