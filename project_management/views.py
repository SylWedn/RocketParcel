from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

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
    data = {
        'title': 'index page',
        'menu': menu,
        'posts': data_db
    }

    return render(request, 'index.html', context=data)


def about(request):
    return render(request, 'about.html', {'title': 'about web'})


def show_post(request, id):
    return HttpResponse(f"Post #{id}")


def add_page(request):
    return HttpResponse("Add page")


def contact(request):
    return HttpResponse("Contact page")


def login(request):
    return HttpResponse("Login page")
