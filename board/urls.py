from django.urls import path
from .views import index,create,detail,update,delete,create_comment,comment_delete,like,com_like

urlpatterns = [
    path('',index, name="index" ),
    path('create/',create, name="create" ),
    path('detail/<int:post_id>',detail, name="detail" ),
    path('update/<int:post_id>',update, name="update" ),
    path('delete/<int:post_id>',delete, name="delete" ),
    path('create_comment/<int:post_id>', create_comment, name="create_comment"),
    path('comment_delete/<int:post_id>/<int:com_id>', comment_delete, name="comment_delete"),
    path('like/<int:post_id>/', like, name="like"),
    path('com_like/<int:com_id>/<int:post_id>', com_like, name='com_like'),


]
