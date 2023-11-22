from django.contrib import admin
from django.urls import path,include


from bulletinboard import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.article_list, name='article_list'),
    path('<int:ad_id>/', views.article_detail, name='article_detail'),
    path('accounts/', include('allauth.urls')),
    path('search/', views.search, name='search'),
    path('create_article/', views.create_article, name='create_article'),
]