from django.db import models
from django.utils import timezone

class Post(models.Model) :
    title = models.CharField(max_length = 200) #제목
    author = models.CharField(max_length = 200) #작성자
    pub_date = models.DateTimeField(default  = timezone.now) #작성일
    image = models.ImageField(upload_to = 'images/') #사진
    body = models.TextField() #내용
    rent_date = models.CharField(max_length =200) #대여가능일
    price = models.PositiveIntegerField() #가격
    choice_parcel = models.BooleanField() #택배가능여부
    use = models.TextField() #용도
    region_sido = models.CharField(max_length = 10) #지역(시/도)
    region_sigungu = models.CharField(max_length = 10) #지역(군/구)
    sort = models.CharField(max_length = 10) #기종(캠코더/DSLR/미러리스)
    

    def __str__(self):
      return self.title

<<<<<<< HEAD
=======
class Comment(models.Model) :
    post = models.ForeignKey('mainapp.Post', on_delete=models.CASCADE, related_name = 'comments')
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text

>>>>>>> a62ebfbef2cd79acaffd688a976b41d27c4758a3


