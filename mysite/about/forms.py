from django import forms

from about.models import Post1


class AboutViewF(forms.ModelForm):
    post = forms.CharField(required=True)
    post1 = forms.TextInput(attrs={'class' : 'myfieldclass'})
    class Meta:
        model = Post1
        fields = ('post', 'post1', )

