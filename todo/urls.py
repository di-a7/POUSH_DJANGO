from django.urls import path
from .views import *
urlpatterns = [
   path('index/', index),
   path('home/', home),
   path('todolist/',todolist),
   path('todolist/create/',create_tasks),
   path('todolist/<id>/', mark_complete),
   path('todolist/<id>/edit/', edit),
   path('todolist/<id>/delete/', delete)
]
