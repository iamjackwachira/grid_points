from rest_framework import serializers


class GridPointsSerializer(serializers.Serializer):
    points = serializers.CharField()

    def validate_points(self, points):
        if points:
            try:
                coordinates = points.split(";")
                for coord in coordinates:
                    x, y = coord.split(",")
                    float(x)
                    float(y)
            except ValueError:
                # If any of the points are not valid floats, the string is invalid
                raise serializers.ValidationError("The input string is invalid")
        return points
