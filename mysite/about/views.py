from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from about.forms import AboutViewF
from about.models import Post1


# Create your views here.
class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get(self, request):
        form = AboutViewF()
        posts = Post1.objects.all()
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)


    def post(self, request):
        form = AboutViewF(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = AboutViewF()
            return redirect('about:about')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)