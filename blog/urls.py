from django.urls import path
from .views import home_page, article_page, article_detail_page, about_page

urlpatterns = [
    path('', home_page, name='home'),
    path('article/', article_page, name='article'),
    path('article/<int:pk>/', article_detail_page, name='detail'),
    path('about/', about_page, name='about')



]
