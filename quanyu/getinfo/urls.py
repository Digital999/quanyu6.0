from django.urls import path
from . import views
urlpatterns = [
    path('hotel/',views.get_hotel.as_view()),
    path('xiuxian/',views.get_xiuxian.as_view()),
    path('nongjia/',views.get_nongjia.as_view()),
    path('post_hotel_component/',views.Sumbmmit_hotel_Component.as_view()),
    path('post_user_component/',views.Sumbmmit_user_Component.as_view()),
    path('get_hotel_component/',views.Get_hotel_Component.as_view()),
    path('get_user_component/',views.Get_user_Component.as_view()),
]