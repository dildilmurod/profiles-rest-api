from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serizalizes a name filed for testing our Apiview"""

    name = serializers.CharField(max_length=10)

