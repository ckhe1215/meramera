from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def detail(request):
    return render(request, 'detail.html')

def result(request):
    return render(request, 'result.html')

def write(request):
    return render(request, 'write.html')

def mypage(request):
    return render(request, 'mypage.html')

def review_board(request):
    return render(request, 'review/review_board.html')

def review_detail(request):
    return render(request, 'review/review_detail.html')

def review_write(request):
    return render(request, 'review/review_write.html')