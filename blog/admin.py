from django.contrib import admin
from .models import Category, Article, Contact, Comments


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'auth', 'body'[:30])


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'body')


admin.site.register(Category)
admin.site.register(Contact)



