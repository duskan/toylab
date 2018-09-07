from django.http import HttpResponseRedirect

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView

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


class PostCreateView(FormView):
    model = Post
    template_name = "post/create.html"
    form_class = PostCreateForm
    #
    # def get_form_kwargs(self):
    #     kwargs = super(PostCreateView, self).get_form_kwargs()
    #     # kwargs.update({'user': self.request.user})
    #     return kwargs
