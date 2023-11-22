from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Article


from .forms import SearchForm
from .forms import ArticleForm



def article_list(request):
    bulletinboard = Article.objects.all()
    return render(request, 'flatpages/article_list.html', {'bulletinboard': bulletinboard})

def article_detail(request, article_id):
    bulletinboard = Article.objects.get(id=article_id)
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
            return redirect('bulletinboard_list')
    else:
        form = ArticleForm()
    return render(request, 'flatpages/create_article.html', {'form': form})

