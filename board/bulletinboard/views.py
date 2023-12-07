from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import (ListView,DetailView,CreateView,DeleteView,UpdateView)
from django.views.generic.edit import CreateView



from .models import Article,Profile


from .forms import SignUpForm,SearchForm,ArticleForm





def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def base(request):
    bulletinboard = Article.objects.all()
    return render(request, 'base.html', {'bulletinboard': bulletinboard})

def article_list(request):
    article = Article.objects.all()
    return render(request, 'flatpages/article_list.html', {'article': article})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'flatpages/article_detail.html', {'article': article})


def search(request):
    bulletinboard = Article.objects.all()
    form = SearchForm(request.GET)

    if form.is_valid():
        query = form.cleaned_data['query']
        bulletinboard = bulletinboard.filter(title__icontains=query)

    return render(request, 'flatpages/search.html', {'form': form, 'bulletinboard': bulletinboard})




def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('bulletindoard_list')
    else:
        form = ArticleForm()
    return render(request, 'flatpages/create_article.html', {'form': form})


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'