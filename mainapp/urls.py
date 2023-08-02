from django.urls import path

from .apps import MainappConfig
from . import views as mainapp_views

app_name = MainappConfig.name

urlpatterns = [
    path('', mainapp_views.MainPageView.as_view(), name='main_page'),
    path('new/', mainapp_views.NewTaskPAgeView.as_view(), name='new_task'),
    path('task/<int:pk>', mainapp_views.DetailTask.as_view(), name='task'),
]
