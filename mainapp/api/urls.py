from django.urls import path

from rest_framework import routers

from .views_api import (BlogCategoryViewSet, BlogPostViewSet, TestAPIView, )

# Маршрутизация через 'routers', для класса 'viewsets'
router = routers.SimpleRouter()
router.register('category', BlogCategoryViewSet, basename='category')
router.register('blogpost', BlogPostViewSet, basename='blogpost')

urlpatterns = [
    # path('test-api/', TestAPIView.as_view(), name='test_api'),
]

urlpatterns += router.urls
