"""mb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from articles.views import ArticlesHomeView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCreateView, SubmitArticle

urlpatterns = [
    path('article-list/', ArticlesHomeView.as_view(), name="articles"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name="article_delete"),
    path('add-article/', ArticleCreateView.as_view(), name="article_create")

]
