from django.urls import path

from blog.views import index, PostListView, PostDetailView, PostCreateView

urlpatterns = [
    # ex: /polls/
    path('', index, name='index'),
    path('post/', PostListView.as_view(), name='post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/create', PostCreateView.as_view(), name='post-create'),
    # ex: /polls/5/
]
