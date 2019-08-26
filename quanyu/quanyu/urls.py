"""quanyu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.views import static
from .settings import MEDIA_ROOT
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
urlpatterns = [
    path('quanyu/admin/', admin.site.urls),
    path('quanyu/user/',include('user.urls')),
    path('quanyu/hotel/',include('hotelinfo.urls')),
    path('quanyu/food/',include('foodinfo.urls')),
    path('quanyu/scenic/',include('scenicinfo.urls')),
    path('quanyu/hotelinfo/',include('getinfo.urls')),
    path('quanyu/getinfo/',include('getinfo.urls')),
    path('quanyu/analyze/',include('analyze.urls')),
    path('quanyu/docs/',schema_view),
    path('quanyu/share/',include('share.urls')),

    # url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # url('^static/(?P<path>.*)$',static.serve,{'document_root':settings.STATIC_ROOT},name='static')
]
