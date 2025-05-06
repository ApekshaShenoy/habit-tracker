from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('add/', views.add_habit, name='add_habit'),
    path('complete/<int:habit_id>/', views.mark_as_done, name='mark_as_done'),
]
