from django.urls import path
from . import views

urlpatterns = [
    path('dev_in/<int:dev_in_code>', views.dev_input),  # http://127.0.0.1:8000/dev_input/
]