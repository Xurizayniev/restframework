from rest_framework import serializers
from .models import TodoModel

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoModel
        fields = '__all__'

    def create(self, validated_data):
        return TodoModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance
