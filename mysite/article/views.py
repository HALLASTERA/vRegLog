from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from article.forms import FormArticle
from article.models import ModelArticle



class ArticleView(TemplateView):

    template_name = 'article/article.html'


    def get(self, request):
        form = FormArticle()
        show = ModelArticle.objects.all()

        return render(request, self.template_name, {'form': form, 'show': show})



# Create your views here.
