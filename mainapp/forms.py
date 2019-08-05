from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','pub_date','image','body','rent_date','price','choice_parcel','use','region_sido','region_sigungu','sort',)


class CommentForm(forms.ModelForm):
    class Meta:
        models = Comment
        fields = ('text', )