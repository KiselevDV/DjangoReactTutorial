from django.contrib import admin

from .models import BlogCategory, BlogPost

admin.site.register(BlogCategory)
admin.site.register(BlogPost)

admin.site.site_header = 'Блог на Django и React'
admin.site.site_title = 'SPA'
