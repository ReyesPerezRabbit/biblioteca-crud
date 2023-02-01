from django.urls import path
from .views import blog_publicaciones


urlpatterns = [
    path('', blog_publicaciones, name="blog_publicaciones")
]