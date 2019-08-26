from django.urls import path
from . import views
urlpatterns = [
    #base_url:djt616.cn:5001:/analyze/
    #data={ 'dizhi':'涟源'}
    path('age/',views.age_analyze.as_view()),
    path('team/',views.team_analyze.as_view()),
    path('staytime/',views.staytime_analyze.as_view()),
    path('from/',views.from_analyze.as_view()),
    path('method/',views.method_analyze.as_view()),
    path('tools/',views.tools_analyze.as_view()),
]