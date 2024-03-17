from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from django.contrib import auth
from accounts.serializers import UserSerializer



class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user
        try:
            isAuthenticated = user.is_authenticated
            
            if isAuthenticated:
                return Response({'isAuthenticated': 'Success'})
            else:
                return Response({'isAuthenticated': 'error'})
        except:
            return Response({'error': 'Something went wrong while checking authentication status'})



@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        username = data['username']
        password = data['password']
        re_password = data['re_password']
        try:
            if password == re_password:
                
                if User.objects.filter(username = username).exists():
                    return Response({'error': 'Username already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 characters'})
                    else:
                        user = User.objects.create_user(username = username, password=password)
                        
                        user = User.objects.get(id=user.id)
                        user_profile = UserProfile.objects.create(user=user, first_name='',last_name='',profile_image=None, phone='',city='')
                        return Response({'success': 'User created successfully'})

            else:
                return Response({'error': 'Pssword do not match'})
        except:
            return Response({'error': 'something went wrong while registration'})
        
 
@method_decorator(csrf_protect, name='dispatch') 
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        data = self.request.data
        
        username = data['username']
        password = data['password']
        try:
            user = auth.authenticate(username = username, password=password)
            if user is not None:
                auth.login(request, user)
                return Response({'success': 'User authenticated'})
            else:
                return Response({'error': 'Error Authenticating'})
        except:
            return Response({'error': 'Something went wrong while logging in'})
class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success': 'Logged Out'})
        except:
            return Response({'success': 'Something went wrong while logging out'})
        

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )
    
    
    def get(self, request, format=None):
        return Response({'success':'CSRF Cookie set'})
    
    
    
@method_decorator(csrf_protect, name='dispatch')     
class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user
        try:
            user = User.object.filter(id=user.id).delete()
            
            return Response({'success':'User deleted successfully'})
        except:
            return Response({'Error': 'Somethoing went worng while deleting account'})
    
class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, format=None):
        users = User.objects.all()
        
        users = UserSerializer(users, many=True)
        return Response(users.data)

    
    
    
    
