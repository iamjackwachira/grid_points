import logging

from django.db import transaction

from grid_points.core.exceptions import ApplicationError
from grid_points.core.models import GridPoint
from grid_points.core.utils import calculate_closest_points

logger = logging.getLogger(__name__)


@transaction.atomic
def find_closest_points(received_points: str) -> str:
    try:
        closest_points = calculate_closest_points(received_points)
    except Exception as e:
        logger.error(e)
        raise ApplicationError(message="Error calculating closest points")

    GridPoint.objects.create(
        received_points=received_points, closest_points=closest_points
    )
    return closest_points
