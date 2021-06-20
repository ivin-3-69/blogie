from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path("category/<str:category>", views.blog_category, name="blog_category"),
    path("<int:pkey>", views.blog_detail, name="blog_detail"),

]