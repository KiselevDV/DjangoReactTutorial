from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    BlogCategorySerializer, BlogCategoryDetailSerializer, BlogPostSerializer,
    BlogPostListRetrieveSerializer,
)
from ..models import BlogCategory, BlogPost


class TestAPIView(APIView):
    """Тестовый пример - отдать словарь на фронт"""

    def get(self, request, *args, **kwargs):
        data = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        return Response(data)


class BlogCategoryViewSet(viewsets.ModelViewSet):
    """Вывод всех категорий"""
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

    # Другие сериалиализаторы, для своих случаев
    action_to_serializer = {
        'retrieve': BlogCategoryDetailSerializer
    }

    def get_serializer_class(self):
        """
        Определение сериализатора для своего случая.
        Последовательно пытается применить каждый из тюпла get()
        """
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class BlogPostViewSet(viewsets.ModelViewSet):
    """Вывод всех статей"""
    queryset = BlogPost._base_manager.all()
    serializer_class = BlogPostSerializer

    action_to_serializer = {
        # При запросе на все объекты
        'list': BlogPostListRetrieveSerializer,
        # При запросе на один объект
        'retrieve': BlogPostListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
