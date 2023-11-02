from django.urls import path
from . import views

urlpatterns = [

    path('dev_out/', views.dev_output),  # http://127.0.0.1:8000/dev_input/
    path('send_command/', views.send_command_to_pico, name='send_command_to_pico'),

]