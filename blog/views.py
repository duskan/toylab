from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from blog.models import Post
from blog.forms import PostCreateForm


# Create your views here.
def index(request):
    return HttpResponseRedirect('post')


class PostListView(ListView):
    template_name = "post/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "post/detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "post/create.html"
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post')
