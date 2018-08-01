from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.successView, name='success'),
    path('categories/<slug>/', views.CategoryView.as_view(), name='categories'),
    path('blog/', views.BlogArchiveView.as_view(), name='archive'),
    path('blog/<slug>/', views.EntryView.as_view(), name='detail'),
    path('year/<int:year>/', views.yearView, name='year'),
    path('year/<int:year>/<int:month>/', views.monthView, name='month'),

]
