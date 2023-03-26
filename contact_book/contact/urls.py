from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='contact.index'),
    path('view/<int:id>', views.view, name='contact.view'),
    path('create/', views.create, name='contact.create'),
    path('edit/<int:id>', views.edit, name='contact.edit'),
    path('delete/<int:id>', views.delete, name='contact.delete'),
]
