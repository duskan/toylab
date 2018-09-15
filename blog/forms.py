from django import forms

from blog.models import Post

class PostCreateForm(forms.ModelForm):
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

    # def save(self, user, commit=True):
    #     post = super(PostCreateForm, self).save(commit=False)
    #     title = self.cleaned_data.get('title')
    #     if title:
    #         post.title = title
    #     subtitle = self.cleaned_data.get('subtitle')
    #     if subtitle:
    #         post.subtitle = subtitle
    #     # secret = self.cleaned_data.get('secret')
    #     # if secret:
    #     #     post.secret = secret
    #
    #     post.save()
    #     return post
