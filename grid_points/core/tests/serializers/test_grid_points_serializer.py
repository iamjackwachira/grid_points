from django.test import TestCase
from rest_framework.exceptions import ValidationError

from grid_points.core.serializers import GridPointsSerializer


class GridPointsSerializerTests(TestCase):
    def test_invalid_input_data_type(self):
        serializer = GridPointsSerializer(data={"points": 123})
        self.assertFalse(serializer.is_valid())

    def test_valid_input_string(self):
        serializer = GridPointsSerializer(data={"points": "1.0,2.0;3.0,4.0"})
        self.assertTrue(serializer.is_valid())

    def test_empty_input(self):
        serializer = GridPointsSerializer(data={"points": ""})
        self.assertFalse(serializer.is_valid())

    def test_non_numeric_input(self):
        serializer = GridPointsSerializer(data={"points": "1,2,3"})
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_missing_values(self):
        serializer = GridPointsSerializer(data={"points": "1.0;3.0,4.0"})
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
