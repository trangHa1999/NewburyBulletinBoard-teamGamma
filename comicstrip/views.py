from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Comic
from django.shortcuts import render, redirect, get_object_or_404

class ComicstripListView(LoginRequiredMixin, ListView):
    model = Comic
    template_name = "comicstrip/list.html"
    login_url = 'login'

class ComicstripCreateView(LoginRequiredMixin, CreateView):
    model = Comic
    fields = ['title', 'image', 'summaryText',]
    template_name = "comicstrip/create.html"
    login_url = 'login'
    success_url = reverse_lazy('listComics')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ComicstripRemoveView(LoginRequiredMixin, DeleteView):
    model = Comic
    template_name = "comicstrip/remove.html"
    success_url = reverse_lazy('listComics')
    login_url = 'login'

