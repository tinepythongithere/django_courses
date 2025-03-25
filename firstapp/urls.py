from django.urls import path
from .views import home, list_articles, details_article

app_name = 'firstapp'

urlpatterns = [
    path('home/', home, name='home'),
    path('article/', list_articles, name='articles'),
    path('detail_article_<int:id_article>', details_article, name='details')
]