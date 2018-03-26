from django.conf.urls import url
from blog.views import *


urlpatterns = [

    # Example : /
    url(r'^$', PostListView.as_view(), name='index'),

    # Example : /post/ (same as /)
    url(r'^post/$', PostListView.as_view(), name='post_list'),

    # Example : /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_detail'),

    # Example : /archive/
    url(r'^archive/$', PostArchiveIndexView.as_view(), name='post_archive'),

    # Example : /2012/
    url(r'^(?P<year>\d{4})/$', PostYearArchiveView.as_view(), name='post_year_archive'),

    # Example : /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMonthArchiveView.as_view(), name='post_month_archive'),

    # Example : /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDayArchiveView.as_view(), name='post_day_archive'),

    # Example : /today/
    url(r'^today/$', PostTodayArchiveView.as_view(), name='post_today_archive'),

]