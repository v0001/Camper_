from django.db import models
from django.utils import timezone

#장고의 유저 모델을 사용하기 위함.
from django.conf import settings


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               null=True,
                               related_name="created_posts")
    # user.post_set ==> user.created_posts

    title = models.CharField("제목", max_length=50)

    #백패킹, 차박, 오토캠핑
    # camp_type = models.CharField("캠프 타입", max_length=20,default = '')
    camp_type_choice = (
		('백패킹', '백패킹'),
        ('차박', '차박'),
        ('오토캠핑', '오토캠핑'))
    camp_type = models.CharField("캠프 타입", max_length=20, choices=camp_type_choice)

    desc = models.TextField("내용")     #사진 포함. photo = models.ImageField("사진", blank=True)
    
    ## MAP API 에서 받아야할 정보
    #위도, 경도
    position_latitude = models.FloatField("위도", null=True, blank=True, default=None)
    position_longitude= models.FloatField("경도", null=True, blank=True, default=None)
    #소재지도로명주소 또는 소재지지번주소
    address=models.CharField("주소", max_length=200,default = '')

    #화장실, 샤워실, 취사장, 매점, 전기시설, 상하수시설, 화재관련시설
    facility_toilet = models.BooleanField("화장실", default=False)
    facility_showerroom = models.BooleanField("샤워실",default=False)
    facility_cookroom = models.BooleanField("취사장", default=False)
    facility_store = models.BooleanField("매점", default=False)
    facility_electric = models.BooleanField("전기시설", default=False)
    facility_water_sewage = models.BooleanField("상하수시설", default=False)
    facility_fire = models.BooleanField("화재관련시설", default=False)
    #야영 가능한 사이트 수. 항상 주차해야한다고 가정.
    capacity = models.FloatField("야영 가능한 사이트 수", null=True, blank=True, default=None)
    #최소이용가격, 최대이용가격
    price_min=models.FloatField("최소이용가격", null=True, blank=True, default=None)
    price_max=models.FloatField("최대이용가격", null=True, blank=True, default=None)

    # 좋아요
    like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                  related_name="liked_posts")
    # user.post_set ==> user.liked_posts
    create_at = models.DateTimeField('처음작성시각', default=timezone.now)
    #update_at = models.DateTimeField('마지막수정시각', default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               null=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    #1:N, onetomany,
    desc = models.CharField("댓글", max_length=200)

    like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                  related_name="liked_com")

    create_at = models.DateTimeField('작성시간', default=timezone.now)

    def __str__(self):
        return self.desc
