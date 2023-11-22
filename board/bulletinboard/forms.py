from django import forms

from .models import Article



class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)



class ArticleForm(forms.ModelForm):
    class Meta:
     model = Article
     fields = ['author','title', 'text', 'category', 'upload']

