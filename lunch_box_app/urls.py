from django.urls import path

from .views import index, my_lunch_box

urlpatterns = [
    path('', index, name='index'),
    path('lunch_box_app', my_lunch_box, name='my_lunch_box')
]