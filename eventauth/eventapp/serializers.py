from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_name','date', 'time','location','image','specification','outcomes' ,'is_liked')