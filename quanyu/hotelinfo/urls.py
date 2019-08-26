from django.urls import path
from . import views
urlpatterns = [
     path('analyze/',views.hotel_analyze.as_view()),
]