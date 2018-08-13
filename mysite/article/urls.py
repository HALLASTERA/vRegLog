from django.urls import path
from article.views import ArticleView


app_name = 'article'

urlpatterns = [

    path('', ArticleView.as_view(), name='article'),
]