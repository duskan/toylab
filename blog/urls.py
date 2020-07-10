from django.urls import path

from blog.views import (index, get_webhook, PostListView, PostDetailView, PostCreateView,
                        NotImplementsView, PostUpdateView)

urlpatterns = [
    # ex: /polls/
    path('', index, name='index'),
    path('get_webhook', get_webhook, name='get_webhook'),
    path('post/', PostListView.as_view(), name='post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/create', PostCreateView.as_view(), name='post-create'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post-update'),
    # ex: /polls/5/
    path('not_implements/', NotImplementsView.as_view(), name='not_implements'),
]
