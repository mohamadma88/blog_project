from django.shortcuts import render, get_object_or_404
from blog.forms import ContactForm, MessageForm
from blog.models import Article
from django.views.generic import DetailView, ListView


def post_detail(request, slug):
    detail = get_object_or_404(Article, slug=slug)

    return render(request, 'blog/blog-details.html', {'detail': detail})


class ArticleList(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()
    context_object_name = 'article_list'
    paginate_by = 2


def contact(request):
    if request.method == 'POST':
        contactus = MessageForm(data=request.POST)

        if contactus.is_valid():
            contactus.save()
    else:
        contactus = MessageForm
    return render(request, 'blog/contact.html', context={'contact': contactus})
