from django.urls import path
from coursesupport.views import CoursesHomeView, CourseUpdateView, CourseDetailView, CourseDeleteView

urlpatterns = [
    path('', CoursesHomeView.as_view(), name="course"),
    path('<int:pk>/edit/', CourseUpdateView.as_view(), name="course_edit"),
    path('<int:pk>/', CourseDetailView.as_view(), name="course_detail"),
    path('<int:pk>/delete', CourseDeleteView.as_view(), name="course_delete"),
]
