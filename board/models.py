from django.db import models
from django.utils import timezone

#장고의 유저 모델을 사용하기 위함.
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="created_posts" )
    # user.post_set ==> user.created_posts 
    
    title = models.CharField("제목", max_length=50)
    desc = models.TextField("내용")
    
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_posts")
    # user.post_set ==> user.liked_posts 
    create_at = models.DateTimeField('작성시간', default = timezone.now)
    
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True )

    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    #1:N, onetomany, 
    desc = models.CharField("댓글",max_length=200)
    
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_com")

    create_at = models.DateTimeField('작성시간', default = timezone.now)

    def __str__(self):
        return self.desc