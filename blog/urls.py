from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path('new/', views.create_post, name="create-post")
]
