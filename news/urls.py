from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import NewsList, NewsCreate, NewsDelete, CategoryListView, subscribe

urlpatterns =[
    path('', NewsList.as_view(), name='post_list'),
    path('', <int:pk/>, NewDetail.as_view(), name='post_detail'),
    path('search', NewsList.as_view(), name = 'post_list'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete')
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('admin/', admin.site.urls),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('author_now/', author_now, name='author_now'),
    path('categories/<init:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]