from django.urls import path,include
from .views import AddEventView, GetEventView

urlpatterns = [
    path('addevent', AddEventView.as_view()),
    path('getallevent', GetEventView.as_view()),
]