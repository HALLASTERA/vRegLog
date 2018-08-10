from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from article.forms import FormArticle
from article.models import ModelArticle



class ArticleView(TemplateView):

    template_name = 'article/article.html'


    def get(self, request):
        form = FormArticle()
        show = ModelArticle.objects.all()
        return render(request, self.template_name, {'form': form, 'show': show}) #




    def post(self, request):

        form = FormArticle(request.POST)
        if form.is_valid():
            form.save(commit=False )
            text = form.cleaned_data['title']

        args = {'form': form, 'text': text}

        return render(request, self.template_name, args)




 #       form = FormArticle(request.POST)
   #     text = form.save(['title', 'bodytetext'])
  #      args = {'form':form, 'text':text}
  #      return render(request, self.template_name, {'form': form, 'text': text})

# Create your views here.