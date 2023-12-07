from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from allauth.account.forms import SignupForm



from .models import Article



class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)




class ArticleForm(forms.ModelForm):
    class Meta:
     model = Article
     fields = ['author','title', 'text', 'category' ]



class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        help_text='Номер телефона. Формат +7910...', label='test'
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Одна большая буква и т.д.',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2',)



