from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
    
class Post(models.Model):
    result = models.CharField(max_length=100)

class User_Chat(models.Model):
    user = models.CharField(max_length=100)
    total = models.IntegerField(null=True, blank=True)
    
class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.IntegerField(default=0)
    userId = models.ForeignKey('User_Chat', blank=True, on_delete=models.CASCADE)
    
# web-app
# web-app
class Reserve(models.Model):
    DIARY = [
        ('yes', 'open'),
        ('no', 'close'),
    ]
    CENTER_EXP = [
        ('yes', 'yes'),
        ('no', 'no')
    ]
    SEX = [
        ('male', '남성'),
        ('female', '여성'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    nick = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, choices=SEX, default='male')
    # center = models.CharField() 리스트를 api로 받아올텐데 어떻게 해야할지 나중에 생각
    diary_open = models.CharField(max_length=3,choices=DIARY, default='yes')
    center_exp = models.CharField(max_length=3,choices=CENTER_EXP, default='no')
    about = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
class Additional(models.Model):
    SCHOOL=[
        ('elementary', '초등학교 졸업'),
        ('middle', '중학교 졸업'),
        ('high', '고등학교 졸업'),
        ('college', '대학교(2년제)졸업'),
        ('university', '대학교(4년제)졸업'),
        ('graduate', '대학원 졸업 이상'),
        ('others', '기타'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.CharField(max_length=10, choices=SCHOOL, default='elementary', null=True, blank=True)
    school_others = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    parent = models.CharField(max_length=2, null=True, blank=True)
    reason = models.CharField(max_length=100, null=True, blank=True)
    sibling = models.CharField(max_length=10, null=True, blank=True)
    marriage = models.CharField(max_length=3, null=True, blank=True)
    child = models.CharField(max_length=3, null=True, blank=True)
    child_num = models.CharField(max_length=10, null=True, default='0')
    date = models.DateTimeField(default=timezone.now)
    
    
class Diary(models.Model):
    EMOTION = [
        ('기쁨', '기쁨'),
        ('혐오', '혐오'),
        ('두려움', '두려움'),
        ('분노', '분노'),
        ('슬픔', '슬픔'),
        ('기타', '기타'),
    ]
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    situation = models.TextField(default="")
    emotion = models.CharField(max_length=3, choices=EMOTION, default='기쁨')
    other = models.CharField(max_length=100, default='', null=True, blank=True)
    score = models.IntegerField()
    detail = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

     