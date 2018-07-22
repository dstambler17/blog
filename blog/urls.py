from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='categories'),
    path('archive/', views.BlogArchiveView.as_view(), name='archive'),
    path('blog/<int:pk>/', views.EntryView.as_view(), name='detail'),

]
