from rest_framework import serializers
from .models import Jog, Datapoint


class JogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jog
        fields = ('start', 'end')


class DatapointSerializer(serializers.ModelSerializer):
    jog = JogSerializer(read_only=True)

    class Meta:
        model = Datapoint
        fields = ('jog', 'coordTime', 'coords')
