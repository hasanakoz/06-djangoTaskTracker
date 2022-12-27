from rest_framework import serializers
from .models import Tasktracker


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasktracker
        fields = (
            'id',
            'task',
            'description',
            'priority',
            'is_done',
            'created_date',
        )
