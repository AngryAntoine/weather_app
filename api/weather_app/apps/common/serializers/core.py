from rest_framework import serializers


class CoreSerializer(serializers.Serializer):
    def create(self, validated_data):
        assert False, "Do not use create directly"

    def update(self, instance, validated_data):
        assert False, "Do not use update directly"
