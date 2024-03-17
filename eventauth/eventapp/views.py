from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Event
from django.views.decorators.csrf import csrf_protect
from .serializers import EventSerializer
from rest_framework import permissions
from django.utils.decorators import method_decorator
import logging
from rest_framework import status


logger = logging.getLogger(__name__)

@method_decorator(csrf_protect, name='dispatch')
class AddEventView(APIView):
    def post(self, request, format=None):
        serializer = EventSerializer(data=self.request.data)
        try:
            if serializer.is_valid():
                user = self.request.user
                event = serializer.save(user=user)
                serialized_data = EventSerializer(event)
                return Response({'success': 'Event added Successfully'})
            else:
                print(self.request.user)
                return Response({'error': 'Error occurred while adding event'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("An error occurred during adding event: %s" % str(e))
            return Response({'error': 'An error occurred during adding event'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class GetEventView(APIView):
    def get(self, request):
        try:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response({'success':serializer.data})
        except:
            return Response({'error': 'Failed to get events'})