from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from blog.models import Post
from blog.forms import PostCreateForm
from django.http.response import JsonResponse


# Create your views here.
def index(request):
    return HttpResponseRedirect('post')


def get_webhook(request):
    if request.method == "POST":
        print("request_data", request.POST)

    return JsonResponse({'status': 'success'})


class NotImplementsView(TemplateView):
    template_name = "not_implements.html"


class PostListView(ListView):
    template_name = "post/list.html"
    model = Post
    ordering = ['-ctime']

    # def get_queryset(self, *args, **kwargs):
    #     super(PostListView, self).get(get_queryset)


class PostDetailView(DetailView):
    template_name = "post/detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "post/create.html"
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post')


class PostUpdateView(UpdateView):
    template_name = "post/create.html"
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post')
