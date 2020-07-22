from django import forms
from blogapp.models import Post

class FormFill(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','post','author')
