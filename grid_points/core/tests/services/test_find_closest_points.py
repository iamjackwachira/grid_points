from django.test import TestCase

from grid_points.core.services import find_closest_points


class FindClosestPointsTests(TestCase):
    def test_closest_points(self):
        points = "2,2;-1,30;20,11;4,5"
        self.assertEqual(find_closest_points(points), "2,2;4,5")

    def test_single_point(self):
        points = "1,1"
        self.assertEqual(find_closest_points(points), "")

    def test_same_distance_points(self):
        points = "2,2;4,4;-2,-2;1,5"
        self.assertIn(find_closest_points(points), ["2,2;4,4", "-2,-2;1,5"])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            find_closest_points("2,2;4,x")

    def test_empty_input(self):
        self.assertEqual(find_closest_points(""), "")

    def test_same_point_input(self):
        self.assertEqual(find_closest_points("3,4;3,4"), "3,4;3,4")

    def test_duplicate_points(self):
        points = "1,1;2,2;2,2;3,3"
        self.assertIn(find_closest_points(points), ["1,1;2,2", "2,2;2,2", "2,2;3,3"])

    def test_collinear_points(self):
        points = "1,1;2,2;3,3"
        self.assertEqual(find_closest_points(points), "1,1;2,2")

    def test_only_two_points(self):
        self.assertEqual(find_closest_points("1,2;4,5"), "1,2;4,5")
