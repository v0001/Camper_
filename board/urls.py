from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('write/', write, name="write"),
    path('detail/<int:post_id>', detail, name="detail"),
    path('update/<int:post_id>', update, name="update"),
    path('delete/<int:post_id>', delete, name="delete"),
    path('create_comment/<int:post_id>', create_comment,name="create_comment"),
    path('comment_delete/<int:post_id>/<int:com_id>',comment_delete, name="comment_delete"),
    path('like/<int:post_id>/', like, name="like"),
    path('com_like/<int:com_id>/<int:post_id>', com_like, name='com_like'),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)