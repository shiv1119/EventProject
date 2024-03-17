# from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile
from .serializers import UserProfileSerializer


class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username
            
            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)
            
            return Response({'profile ': user_profile.data , 'username': str(username)})
        except:
            return Response({'error':'Something went wrong while retriving user data'})
            
            
    
    
class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            username = user.username
            data = self.request.data
            first_name = data['first_name']
            last_name = data['last_name']
            profile_image = data['profile_image']
            phone = data['phone']
            city = data['city']
        
            UserProfile.objects.filter(user=user).update(first_name=first_name, last_name=last_name, profile_image=profile_image, phone=phone, city=city)
            
            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)
            
            return Response({'profile ': user_profile.data , 'username': str(username)})
        except:
            return Response({'error':'Error occoured during profile updation'})