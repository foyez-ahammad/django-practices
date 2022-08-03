from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('c', views.create, name='create'),
    path('u/<int:id>/', views.delete, name='delete'),
    path('<int:id>/', views.update, name='update'),

]