from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'placeholder': "닉네임",
            'class': 'for_maker_nick'})
        self.fields['body'].widget.attrs.update(
            {'placeholder': '제작자에게 한마디',
            'class': 'for_maker_desc'})
            
    class Meta:
        model = Blog
        fields = ('title', 'body',)