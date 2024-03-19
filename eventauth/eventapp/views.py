from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from .models import Event
from django.views.decorators.csrf import csrf_protect
from .serializers import EventSerializer
from rest_framework import permissions
from django.utils.decorators import method_decorator
from rest_framework import status



@method_decorator(csrf_protect, name='dispatch')
class AddEventView(APIView):
    def post(self, request, format=None):
        serializer = EventSerializer(data=self.request.data)
        if serializer.is_valid():
            try:
                user = self.request.user
                event = serializer.save(user=user)
                serialized_data = EventSerializer(event)
                return Response({'success': 'Event added Successfully'})
            except Exception as e:
                print("An error occurred during adding event:", e)
                return Response({'error': 'An error occurred during adding event'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print("Serialization errors:", serializer.errors)
            return Response({'error': 'Error occurred while adding event'}, status=status.HTTP_400_BAD_REQUEST)




class GetEventView(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request):
        try:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response({'success':serializer.data})
        except:
            return Response({'error': 'Failed to get events'})
        
@method_decorator(csrf_protect, name='dispatch')
class GetEventByUserView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username
            user_event_data = Event.objects.filter(user=user)
            if user_event_data.exists():
                user_event_data_serialized = EventSerializer(user_event_data, many=True)
                return Response({'User event data': user_event_data_serialized.data, 'username': str(username)})
            else:
                return Response({'error': 'No events found for the user'})
        except Exception as e:
            return Response({'error': 'Error while getting user event data', 'details': str(e)})
        

class UpdateEventView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            data = self.request.data
            
            # Extracting data from request
            event_name = data.get('event_name')
            date = data.get('date')
            time = data.get('time')
            location = data.get('location')
            image = data.get('image')
            specification = data.get('specification')
            outcomes = data.get('outcomes')
            is_liked = data.get('is_liked')
            
            event_instance = Event.objects.filter(event_name=event_name).first()
            if event_instance:
                event_instance.date = date
                event_instance.time = time
                event_instance.location = location
                event_instance.image = image
                event_instance.specification = specification
                event_instance.outcomes = outcomes
                event_instance.is_liked = is_liked
                event_instance.save()
                event_data = EventSerializer(event_instance)
                return Response({'Success': event_data.data})
            else:
                return Response({'error': 'Event does not exist'})
        except Exception as e:
            return Response({'error': 'Error while updating event data', 'details': str(e)})


class GetRecentlyAddedEventView(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        try:
            recent_events = Event.objects.order_by('-created_at')[:10]
            serializer = EventSerializer(recent_events, many=True)
            return Response({'success':serializer.data})
        except:
            return Response({'error': 'Failed to get Latest Event'})