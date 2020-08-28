from django.shortcuts import render
from faker import Faker

from accounts.models import mypage
from board.models import Post


# Create your views here.
def index(request):
    context = {}
    temp_profile = Faker('ko_KR')
    user = request.user
    
    context= {'boards': Post.objects.all()}

    return render(request, 'map.html',context)


# def map(request):
#     myplace = MyPlace.objects.all()
#     lat = 0
#     long = 0
#     for i in range(92):
#         lat += myplace[i].latitude
#         long += myplace[i].longitude

#     lat = lat/92
#     long = long/92
#     print(lat,long)
#     context = {"myplace": myplace,'lat':lat,'long':long}

#     return render(request, 'map.html',context)


