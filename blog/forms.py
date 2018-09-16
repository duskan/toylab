from django import forms
from martor.fields import MartorFormField

from blog.models import Post

class PostCreateForm(forms.ModelForm):
    # contents = MartorFormField()
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'secret', 'contents']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'title': 'title',
                    'class': 'form-control col-sm-10'
                }
            ),
            'subtitle': forms.TextInput(
                attrs={
                    'title': 'subtitle',
                    'class': 'form-control col-sm-10'
                }
            ),
            'contents': forms.Textarea(
                attrs={
                    'title': 'contents',
                    'class': 'form-control'
                }
            )
        }

    def save(self, commit=True):
        post = super(PostCreateForm, self).save(commit=False)
        contents = self.cleaned_data.get('contents')
        if contents:
            post.contents = contents
    #     subtitle = self.cleaned_data.get('subtitle')
    #     if subtitle:
    #         post.subtitle = subtitle
    #     # secret = self.cleaned_data.get('secret')
    #     # if secret:
    #     #     post.secret = secret
    #
        post.save()
        return post
