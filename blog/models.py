from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    img = models.ImageField(blank=True, null=True)
    imglist = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField()
    quote = models.TextField(null=True, blank=True)
    pub = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail:article', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=5, null=True, blank=True)
    email = models.EmailField()
    sub = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parents = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', blank=True, null=True)
    body = models.TextField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)

