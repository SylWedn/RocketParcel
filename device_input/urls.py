from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^dev_in/(?P<dev_in_code>[0-9]{8})/', views.dev_input),  # http://127.0.0.1:8000/dev_inp/12345678
]

# TODO: dev_in_code treatment for DB, and logic
# TODO: Adapt to temp sensor when installed {8} to {10}
# TODO: check if input is INT, or make converter
