from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='todo.index'),
    path('view/<int:id>', views.view, name='todo.view'),
    path('create/', views.create, name='todo.create'),
    path('edit/<int:id>', views.edit, name='todo.edit'),
    path('delete/<int:id>', views.delete, name='todo.delete'),
]
