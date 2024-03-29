from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','body','rent_date','price','choice_parcel','use','region_sido','region_sigungu','region_rest','sort',)
 
class CommentForm(forms.ModelForm):
    class Meta:
        models = Comment
        fields = ('text', )

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    model = Comment
    fields = ('text', 'is_secret', 'is_accepted')
