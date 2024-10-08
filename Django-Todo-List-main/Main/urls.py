from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('delete_todo/<int:todo_id>',views.delete_todo, name='delete_todo'),
    path('update_todo/<int:todo_id>',views.update_todo, name='update_todo'),
]