from django.contrib import admin
from django.urls import path,include
from allauth.account.views import SignupView

from django.views.generic import RedirectView

from bulletinboard import views

from .views import *
from .views import SignUp




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.base, name='base'),
    path('article_list/', views.article_list, name='article_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('search/', views.search, name='search'),
    path('create_article/', views.create_article, name='create_article'),
    path('signup', SignUp.as_view(), name='signup'),
    path('user/registration/', registration),

]