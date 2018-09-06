from django.urls import path

from blog.views import index, PostListView, PostDetailView

urlpatterns = [
    # ex: /polls/
    path('', index, name='index'),
    path('post/', PostListView.as_view(), name='post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    # ex: /polls/5/
]
