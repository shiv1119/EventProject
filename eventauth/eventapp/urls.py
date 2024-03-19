from django.urls import path,include
from .views import AddEventView, GetEventView, GetEventByUserView,UpdateEventView,GetRecentlyAddedEventView

urlpatterns = [
    path('addevent', AddEventView.as_view()),
    path('getallevent', GetEventView.as_view()),
    path('geteventbyuser', GetEventByUserView.as_view()),
    path('updateevent', UpdateEventView.as_view()),
    path('getlatestevent', GetRecentlyAddedEventView.as_view())
    
]