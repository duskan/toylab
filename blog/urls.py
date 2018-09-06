from django.urls import path

from blog.views import IndexView

urlpatterns = [
    # ex: /polls/
    path('', IndexView.as_view(), name='index'),
    # ex: /polls/5/
]
