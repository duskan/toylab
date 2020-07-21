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

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema

import jwt
import json
import hashlib


# Create your views here.
def index(request):
    return HttpResponseRedirect('post')

@api_view(['POST'])
@csrf_exempt
def get_webhook(request):
    ALGORITHM = "HS256"
    try:
        from blog.secret import SECRET_KEY
    except:
        print("There is no secret file")
        return JsonResponse({'status': 'success'})
    try:
        token = request.META['HTTP_AUTHORIZATION'].split()[1]
    except:
        print("error >> MEATA:", request.META)
        return JsonResponse({'status': 'fail'})
    print("----------------------------------------------------------")
    print(f"resquest ({type(request.data)})>>>")
    print("JWT result >>", jwt.decode(token, SECRET_KEY, ALGORITHM))
    decoded = jwt.decode(token, SECRET_KEY, ALGORITHM)
    print("\t JSON:", json.dumps(request.data))
    print("\t", hashlib.sha256(json.dumps(request.data).encode('utf-8')).hexdigest())
    print("\t", decoded["payload_hash"])
    print(request.data)
    print("----------------------------------------------------------")

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
