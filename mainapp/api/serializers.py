"""
SerializerMethodField - вывод информации об определённом поле
"""
from rest_framework import serializers

from ..models import BlogCategory, BlogPost


class BlogCategorySerializer(serializers.ModelSerializer):
    """Все категории"""

    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogCategoryDetailSerializer(serializers.ModelSerializer):
    """Для получения детальной информации по постам в категориях"""
    posts = serializers.SerializerMethodField()

    @staticmethod
    def get_posts(obj):
        """Добавить поле 'posts'"""
        return BlogPostSerializer(
            BlogPost.objects.filter(blog_category=obj), many=True).data

    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    """Все статьи"""

    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostListRetrieveSerializer(serializers.ModelSerializer):
    """Все статьи, но с расшифровкой поля 'blog_category'"""
    # Переопределение поля
    blog_category = BlogCategorySerializer()

    class Meta:
        model = BlogPost
        fields = '__all__'
