from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^dev_in/(?P<dev_in_code>[0-9]{10})/', views.dev_input),  # http://127.0.0.1:8000/dev_inp/12345678
]


