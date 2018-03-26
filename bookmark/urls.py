from django.conf.urls import url
from bookmark.views import BookmarkListView, BookmarkDetailView


urlpatterns = [
    # Class-based views
    url(r'^$', BookmarkListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDetailView.as_view(), name='detail'),

]