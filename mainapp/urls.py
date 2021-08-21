from django.urls import path

from .views import index, category_detail, post_detail

urlpatterns = [
    path('posts/<int:id>/', post_detail),
    path('category/<int:id>/', category_detail),
    path('', index),
]
