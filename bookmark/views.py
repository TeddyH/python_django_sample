

# Create your views here.
from django.views.generic import DetailView, ListView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkDetailView(DetailView):
    model = Bookmark