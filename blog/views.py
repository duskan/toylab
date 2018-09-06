from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from blog.models import Post


# Create your views here.
def index(request):
    return HttpResponseRedirect('post')


class PostListView(ListView):
    template_name = "post/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "post/detail.html"
    model = Post
