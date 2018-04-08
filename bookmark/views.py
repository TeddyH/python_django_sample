

# Create your views here.
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkDetailView(DetailView):
    model = Bookmark


class FileTestView(TemplateView):
    template_name = 'bookmark/fileTest.html'

