from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["author"]

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title fewer than 5 characters")
        return value

    def validate_description(self, value):
        if len(value.split()) <=5:
            raise serializers.ValidationError("Description is not total fully")
        return value