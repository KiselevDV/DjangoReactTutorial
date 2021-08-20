from django.urls import path

from .views_api import TestAPIView

urlpatterns = [
    path('test-api/', TestAPIView.as_view(), name='test_api'),
]
