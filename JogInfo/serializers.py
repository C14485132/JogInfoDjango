from rest_framework import serializers
from .models import Run, KeyVal


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ('start', 'end')


class KeyValSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyVal
        fields = ('container', 'coordTime', 'coords')
