from django.urls import path
from . import views

urlpatterns = [
    path('', views.well_home, name='well_home'),
    path('signup/' , views.well_signup, name = 'well_signup'),
    path('tasks/' , views.well_tasks, name = 'well_tasks'),
    path('logaut/' , views.well_signout, name = 'well_signout'),
    path('signin/' , views.well_signin, name = 'well_signin'),
    
]