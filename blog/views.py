from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

from blog.models import Post

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class PostListView(ListView):
    template_name = "post/list.html"
    model = Post
