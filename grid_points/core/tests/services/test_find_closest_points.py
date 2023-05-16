from django.test import TransactionTestCase

from grid_points.core.exceptions import ApplicationError
from grid_points.core.models import GridPoint
from grid_points.core.services import find_closest_points


class FindClosestPointsTestCase(TransactionTestCase):
    def test_with_valid_input(self):
        received_points = "1,2;3,4;5,6;7,8"
        with self.assertNumQueries(3):
            closest_points = find_closest_points(received_points)
        self.assertEqual(closest_points, "1,2;3,4")

        created_grid_point = GridPoint.objects.get(received_points=received_points)
        self.assertEqual(created_grid_point.closest_points, closest_points)

    def test_with_invalid_input_value_error(self):
        received_points = "1,2;3,4;x,y"
        with self.assertRaisesMessage(
            ApplicationError, "Error calculating closest points"
        ):
            find_closest_points(received_points)
