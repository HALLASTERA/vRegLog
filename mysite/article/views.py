from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from article.forms import FormArticle
from article.models import ModelArticle, Article

from django.shortcuts import get_object_or_404
from . import urls


class ArticleView(TemplateView):

    template_name = 'article/article.html'


    def get(self, request):
        form = FormArticle()
        show = ModelArticle.objects.all()
        args = {'form': form, 'show': show}
        return render(request, self.template_name, args)


    def post(self, request):
        form = FormArticle(request.POST)
        if form.is_valid():
            sform = form.save(commit=False)
            sform.user = request.user
            sform.save()
            stitle = form.cleaned_data['title']
            sbodytext = form.cleaned_data['bodytext']
            form = FormArticle()
            return redirect('article:article')
        args = {'form': form, 'stitle': stitle, 'sbodytext': sbodytext}
        return render(request, self.template_name, args)



def rush(request, title1_id):
    idobj = get_object_or_404(Article, pk=title1_id)
    template_name = 'article/stran.html'
    args = {'idobj': idobj}
    return render(request, template_name, args)





#def make_published(request, queryset, modeladmin):
 #   queryset.update(status='p')

#make_published.short_description = "We mark selected stories as published"

