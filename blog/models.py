from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Signable(models.Model):
    user = models.ForeignKey(
        User, verbose_name="User",
        null=True,
        on_delete=models.SET_NULL,
        default=1, # Error 날 수 있음. 하지만 개인 블로그에서 쓸꺼라 일단 내비두자
    )
    ctime = models.DateTimeField(
        "Created datetime",
        auto_now_add=True
    )
    mtime = models.DateTimeField(
        "Modified datetime",
        auto_now=True
    )

    class Meta:
        abstract = True

class Post(Signable):
    title = models.CharField(
        '제목',
        max_length=100,
        help_text='제목',
        null=False,
        blank=False,
    )
    subtitle = models.CharField(
        '부제목',
        max_length=100,
        help_text='부제목',
        null=True,
        blank=True,
    )
    contents = models.TextField(
        '컨텐츠',
        help_text='html contents',
        null=False,
        blank=True,
    )
    secret = models.BooleanField(
        default=False,
    )
