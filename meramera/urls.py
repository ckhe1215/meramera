"""meramera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.index, name = 'index'),
    path('search/', mainapp.views.search, name = 'search'),
<<<<<<< HEAD
    path('detail/<int:post_id>/', mainapp.views.detail, name = 'detail'),
=======
    path('<int:post_id>/', mainapp.views.detail, name = 'detail'),
>>>>>>> a97cc16de7909ee4bd7693e39f0b50dcc227cb52
    path('result/', mainapp.views.result, name = 'result'),
    path('write/', mainapp.views.write, name = 'write'),
    path('mypage/', mainapp.views.mypage, name = 'mypage'),
    path('<int:post_id>/comments/', mainapp.views.add_comment, name='add_comment'),
    path('review_board/', mainapp.views.review_board, name = 'review_board'),
    path('review_detail/', mainapp.views.review_detail, name = 'review_detail'),
    path('review_write/', mainapp.views.review_write, name = 'review_write'),
    path('accounts/', include('accounts.urls')),
]
