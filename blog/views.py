from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, YearArchiveView, ArchiveIndexView, MonthArchiveView, \
    DayArchiveView, TodayArchiveView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post


class PostArchiveIndexView(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYearArchiveView(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True


class PostMonthArchiveView(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


class PostDayArchiveView(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTodayArchiveView(TodayArchiveView):
    model = Post
    date_field = 'modify_date'

