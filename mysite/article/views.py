from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from article.forms import FormArticle
from article.models import ModelArticle



class ArticleView(TemplateView):

    template_name = 'article/article.html'


    def get(self, request):
        form = FormArticle()
        show = ModelArticle.objects.all()
<<<<<<< HEAD
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
=======
        return render(request, self.template_name, {'form': form, 'show': show}) #
>>>>>>> dd18c8f4052b49c4ffea99a924b772756bd23d7a




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