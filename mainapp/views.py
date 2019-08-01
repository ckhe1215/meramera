from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def detail(request):
    return render(request, 'detail.html')

def result(request):
    posts = Post.objects
    return render(request, 'result.html' , {'posts' : posts})

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