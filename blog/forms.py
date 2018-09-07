from django import forms

from blog.models import Post


class PostCreateForm(forms.Form):
    title = forms.CharField(
        label='제목',
        required=True,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'title': '제목',
                'class': 'form-control',
            }
        ),
    )
