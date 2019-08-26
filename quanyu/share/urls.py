from django.urls import path,re_path
from django.conf import settings
from django.views.static import serve
from . import views
urlpatterns = [
    path('submmit/',views.Submmit.as_view()),
    path('common/',views.Common_list.as_view()),
    path('waitselect/',views.Waitselect.as_view()),
    path('select/',views.Select.as_view()),
    path('good/',views.Good.as_view()),
    path('keep/',views.Postkeep.as_view()),
    path('getkeep/',views.Getkeep.as_view()),
    path('detail/',views.Singleshare.as_view()),
    path('upload_handle', views.upload_handle),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]