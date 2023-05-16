from rest_framework import serializers


class GridPointsSerializer(serializers.Serializer):
    points = serializers.CharField()
