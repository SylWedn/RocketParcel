from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from .models import Packagedb, Category

# Create your views here.


menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add page', 'url_name': 'addpage'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'Sign in', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'first article', 'content': 'text of first article', 'is_published': True},
    {'id': 2, 'title': 'second article', 'content': 'text of second article', 'is_published': False},
    {'id': 3, 'title': 'third article', 'content': 'text of third article', 'is_published': True}
]


def index(request):
    posts = Packagedb.published.all()
    data = {
        'title': 'index page',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }

    return render(request, 'index.html', context=data)


def about(request):
    return render(request, 'about.html', {'title': 'about web', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Packagedb, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'post.html', context=data)


def add_page(request):
    return render(request, 'add_page.html', {'menu': menu, 'title': 'add page'})



def contact(request):
    return HttpResponse("Contact page")


def login(request):
    return HttpResponse("Login page")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Packagedb.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }

    return render(request, 'index.html', context=data)
