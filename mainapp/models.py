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
    REGION_SIDO_CHOICES = [('Seoul','서울특별시'),('Busan','부산광역시'),('Daegu','대구광역시'),('Incheon','인천광역시'),('Gwangju','광주광역시'),('Daejeon','대전광역시'),('Ulsan','울산광역시'),('Sejong','세종특별자치시'),('Gyeonggi','경기도'),('Gangwon','강원도'),('Chungbuk','충청북도'),('Chungnam','충청남도'),('Jeonbuk','전라북도'),('Jeonnam','전라남도'),('Gyeongbuk','경상북도'),('Gyeongnam','경상남도'),('Jeju','제주특별자치도')]
    region_sido = models.CharField(max_length=30, choices=REGION_SIDO_CHOICES, default= "==========")  #지역(시/도)
    region_sigungu = models.CharField(max_length = 10) #지역(군/구)
    region_rest = models.CharField(max_length = 20) #지역(남은 주소)
    sort = models.CharField(max_length = 10) #기종(캠코더/DSLR/미러리스)
    
    def __str__(self):
      return self.title

class Comment(models.Model) :
    post = models.ForeignKey('mainapp.Post', on_delete=models.CASCADE, related_name = 'comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    is_secret = models.BooleanField()
    is_accepted = models.BooleanField()

    def __str__(self):
        return self.text

