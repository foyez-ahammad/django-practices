from django.urls import path
from . import views

urlpatterns = [
    path('', views.views, name='views'),
    path('adding', views.adding, name='adding'),
    path('/<int:id>/', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('update/<int:id>/', views.search, name='update'),
]
