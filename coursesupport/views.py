from .models import Course
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse

class CoursesHomeView(ListView):
    model = Course
    template_name = "coursesupport/index.html"

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['courseTitle', 'subjectArea', 'articleURL']
    template_name = "coursesupport/course_edit.html"
    login_url = 'login'

class CourseDetailView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['courseTitle', 'subjectArea', 'articleURL']
    template_name = "coursesupport/course_detail.html"
    login_url = 'login'

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = "coursesupport/course_delete.html"
    success_url = reverse_lazy('course')
    login_url = 'login'



