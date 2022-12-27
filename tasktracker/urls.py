from django.urls import path
from .views import (
    task_list_create, 
    task_detail,
    )


urlpatterns = [
    path('list_create', task_list_create),
    path('detail', task_detail),
]