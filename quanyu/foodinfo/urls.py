from django.urls import path
from . import views
urlpatterns=[
    path('info/',views.info_answer.as_view())
]