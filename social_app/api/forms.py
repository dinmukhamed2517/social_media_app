from django import forms
from api.models import Post

class PostForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea( attrs={
        "placeholder": "Enter your post",
        "class": "form-control",
    }),
    label="",)

    class Meta:
        model = Post
        exclude = ('user',)