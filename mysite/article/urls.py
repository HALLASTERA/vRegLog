from django.urls import path
from article.views import ArticleView
from . import views

app_name = 'article'

urlpatterns = [

    path('', ArticleView.as_view(), name='article'),
    path('<int:title1_id>/', views.rush, name='rush'),

]