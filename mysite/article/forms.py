from django import forms
from article.models import ModelArticle


class FormArticle(forms.ModelForm):
    title = forms.CharField()
    bodytext = forms.CharField()
    image = forms.ImageField()

    class Meta:
        model = ModelArticle
        fields = ('title', 'bodytext','image' )