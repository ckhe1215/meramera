from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST ['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('index')
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')