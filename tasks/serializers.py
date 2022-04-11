# DFR imports
from random import choices
from rest_framework import serializers
# elenas import
from .models import Task


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)

class TaskSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True, max_length=75)
    description = serializers.CharField(required=True, max_length=255)
    owner = serializers.ReadOnlyField(source='owner.username')
    status = ChoiceField(required=False, choices=Task.TaskStatus.choices)

    class Meta:
        model = Task
        fields = '__all__'
        ordering = ['title']

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task
        
        