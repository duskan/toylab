from django.urls import path

from blog.views import IndexView, PostListView

urlpatterns = [
    # ex: /polls/
    path('', IndexView.as_view(), name='index'),
    path('post/', PostListView.as_view(), name='post'),
    # ex: /polls/5/
]
