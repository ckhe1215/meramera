from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from .models import Post
from .forms import PostForm
=======
from .models import Post, Comment
>>>>>>> a97cc16de7909ee4bd7693e39f0b50dcc227cb52

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def detail(request, post_id):
    post_detail=get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def result(request):
<<<<<<< HEAD
    posts = Post.objects
    return render(request, 'result.html' , {'posts' : posts})
=======
    post = Post.objects
    return render(request, 'result.html', {'post':post})
>>>>>>> a97cc16de7909ee4bd7693e39f0b50dcc227cb52

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('result')
        else:
            form = PostForm()           
            return render(request, 'write.html', {'form':form})

def mypage(request):
    return render(request, 'mypage.html')

def review_board(request):
    return render(request, 'review/review_board.html')

def review_detail(request):
    return render(request, 'review/review_detail.html')

def review_write(request):
    return render(request, 'review/review_write.html')

def add_comment(request, post_id):
        post=get_object_or_404(Post, pk=post_id)
        if request.method=='POST':
                form=CommentForm(request.POST)
                if form.is_valid():
                        comment=form.save(commit=False)
                        comment.post=post
                        comment.save()
                        return redirect('/post/' + str(post.id))
                else:
                        form=CommentForm()
                return render(request, 'add_comment.html', {'form':form})