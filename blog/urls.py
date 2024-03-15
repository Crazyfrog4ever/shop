from django.urls import path, re_path
from django.urls import register_converter  # Add this line
from . import views
from .extensions.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'blog'
urlpatterns = [
    #ex : hostname/blog
    path('', views.index, name='index'),

    #ex : hostname/blog/5/
    path('<int:post_id>/', views.detail, name='detail'),
    path('archive/<yyyy:year>/', views.archive_year, name='archive'),
]