from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-grade/', views.add_grade, name='add_grade'),
    path('set-goal/', views.set_goal, name='set_goal'),
    path('register/', views.register, name='register'),
    path('complete-goal/<int:goal_id>/', views.complete_goal, name='complete_goal'),
    path('delete-goal/<int:goal_id>/', views.delete_goal, name='delete_goal'), 
]