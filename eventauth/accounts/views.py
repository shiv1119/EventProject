from django.shortcuts import render, Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from user_profile.models import UserProfile


class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        username = data['username']
        password = data['password']
        re_password = data['re_password']
        
        if password == re_password:
            if User.objects.filter(username = username).exists():
                return Response({'error': 'Username already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(username = username, password=password)
                    user.save()
                    
                    user = User.objects.get(username = username)
                    
                    user_profile = UserProfile(user, first_name='',last_name='',profile_image=None, phone='',city='')
                    user_profile.save()
                    return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Pssword do not match'})