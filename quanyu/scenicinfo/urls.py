from django.urls import path
from . import views
urlpatterns = [
     path('info/',views.scenic_info.as_view()),
]