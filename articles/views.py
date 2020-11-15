from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse


class ArticlesHomeView(ListView):
    model = Article
    template_name = "articles/index.html"

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title','summaryText', 'image']
    template_name = "articles/article_edit.html"
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'summaryText']
    template_name = "articles/article_detail.html"
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('articles')
    login_url = 'login'


# TODO This method is a dummy and needs to be re-written.
class SubmitArticle(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'summaryText', 'image', 'articleURL', 'subjectArea']
    template_name = "articles/submit-new-article.html"
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'author', 'image', 'summaryText', 'articleURL', 'vettedBy']
    template_name = "articles/article_create.html"
    login_url = 'login'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.save()
        return HttpResponseRedirect(reverse('articles'))



