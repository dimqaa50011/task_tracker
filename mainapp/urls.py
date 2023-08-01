from django.urls import path

from .apps import MainappConfig
from . import views as mainapp_views

app_name = MainappConfig.name

urlpatterns = [
    path('', mainapp_views.MainPageView.as_view(), name='main_page'),
]
