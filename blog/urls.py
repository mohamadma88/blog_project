from django.urls import path

from . import views
from .views import ArticleList

app_name = 'detail'
urlpatterns = [
    path('detail/<str:slug>', views.post_detail, name='article'),
    path('list/', ArticleList.as_view(), name='list'),
    path('contact/', views.contact, name='contact'),

]