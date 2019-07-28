from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) # user모델 
    name = models.CharField(max_length = 100) # 이름
    phone = models.CharField(max_length = 20) # 연락처
    region_sido = models.CharField(max_length = 10) #지역(시/도)
    region_sigungu = models.CharField(max_length = 10) #지역(군/구)
    profile_pic = models.ImageField(blank = True, upload_to = 'images/profile') # 프로필 사진

    def __str__(self):
        return self.name

    @receiver(post_save, sender = User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender = User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save