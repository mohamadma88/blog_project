from django.contrib import admin
from .models import Category, Article, Contact


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'auth', 'body'[:30])


admin.site.register(Category)
admin.site.register(Contact)

