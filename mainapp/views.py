<<<<<<< HEAD
from django.shortcuts import render
from .models import Post
=======
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
<<<<<<< HEAD
>>>>>>> a62ebfbef2cd79acaffd688a976b41d27c4758a3
=======
from .forms import PostForm
>>>>>>> 8c5225d8b7bc9d73659cb52954ac4b6f1de53cc8

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

<<<<<<< HEAD
def detail(request):
    return render(request, 'detail.html')

def result(request):
    return render(request, 'result.html')

def write(request):
    return render(request, 'write.html')
=======
def detail(request, post_id):
    post_detail=get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def result(request):
    post = Post.objects
    return render(request, 'result.html', {'post':post})

def write(request):
    #if request.method == 'POST':
        post = Post()
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('result')
        else:
            form = PostForm()           
            return render(request, 'write.html', {'form':form})
>>>>>>> a62ebfbef2cd79acaffd688a976b41d27c4758a3

def mypage(request):
    return render(request, 'mypage.html')

def review_board(request):
    return render(request, 'review/review_board.html')

def review_detail(request):
    return render(request, 'review/review_detail.html')

def review_write(request):
<<<<<<< HEAD
    return render(request, 'review/review_write.html')
=======
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
>>>>>>> a62ebfbef2cd79acaffd688a976b41d27c4758a3
