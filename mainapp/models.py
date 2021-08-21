from django.db import models


class BlogCategory(models.Model):
    """Категория"""
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class BlogPostQuerySet(models.QuerySet):
    """
    Кастомный кверисет для менеджера 'BlogPostManager'.
    C методом кверисета 'find_by_title_in_qs', фильтром по title.
    """

    def find_by_title_in_qs(self, post_title):
        return self.filter(title__icontains=post_title)


class BlogPostManager(models.Manager):
    """Кастомный менеджер для модели 'BlogPost'"""

    def get_queryset(self):
        # return super().get_queryset()
        # Заменить на кастомный кверисет
        return BlogPostQuerySet(self.model, using=self._db)

    def all(self):
        """Кастомизация метода 'all'"""
        return self.get_queryset().filter(in_archive=False)

    def find_by_title_in_qs(self, post_title):
        """Кастомный метод у менеджера, аналог методу кверисета"""
        return self.get_queryset().find_by_title_in_qs(post_title)


class BlogPost(models.Model):
    """Статья"""
    blog_category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, verbose_name='Имя категории')
    title = models.CharField(max_length=255, verbose_name='Название поста')
    content = models.TextField(max_length=10000, verbose_name='Содержание')
    image = models.ImageField(
        upload_to='blog_posts/', null=True, blank=True,
        verbose_name='Фото к статье')
    pub_date = models.DateTimeField(
        auto_now=True, verbose_name='Дата публикации')
    in_archive = models.BooleanField(default=False, verbose_name='В архив')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    # Переопределяем objects
    objects = BlogPostManager()

    def __str__(self):
        return f'{self.title} из категории "{self.blog_category.name}"'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
