from django.urls import path
from .views import blog_pu


urlpatterns = [
    path('', blog_pu, name="blog_pu")
]
