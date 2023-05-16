import logging
import math

from django.db import transaction

from grid_points.core.models import GridPoint

logger = logging.getLogger(__name__)


def calculate_closest_points(points: str) -> str:
    """Calculates the points that are closest to each other and returns it

    Args:
        points (str): String of semicolon separated coordinates

    Returns:
        str: String of semicolon separated coordinates
    """

    point_list = points.split(";")

    # Return an empty string if there's only one point or no point to compare
    if len(point_list) < 2:
        return ""

    closest_points = [""] * 2
    min_distance = float("inf")
    point_set = set()

    for i, point1 in enumerate(point_list[:-1]):
        # Skip the calculation between identical points
        if point1 in point_set:
            continue

        x1, y1 = map(float, point1.split(","))

        for point2 in point_list[i + 1 :]:
            # Skip the calculation between a pair of points already compared with
            if point2 in point_set:
                continue

            x2, y2 = map(float, point2.split(","))
            # Calculate the Euclidean distance and compare with the minimimum distance so far
            # https://www.cuemath.com/euclidean-distance-formula/
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if distance < min_distance:
                closest_points = [point1, point2]
                min_distance = distance

        point_set.add(point1)

    return ";".join(closest_points)


@transaction.atomic
def find_closest_points(received_points: str) -> str:
    try:
        closest_points = calculate_closest_points(received_points)
    except ValueError as e:
        logger.error(e)
    except Exception as e:
        logger.error(e)

    GridPoint.objects.create(
        received_points=received_points, closest_points=closest_points
    )
    return closest_points
