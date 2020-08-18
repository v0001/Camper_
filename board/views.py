from django.shortcuts import render,redirect
from .forms import PostForms,CommentForms
from .models import Post,Comment

from django.contrib.auth import get_user_model

from django.db.models import Q #or 조건을 만들기 위한 Q객체


from django.core.paginator import Paginator

User = get_user_model()
# Create your views here.
def index(request):
    context=dict()
    
    search_q = request.GET.get('q','')
    filter_q = request.GET.get('filter','') #filter_q = 오늘
    
    
    search_post = Post.objects.filter(Q(title__icontains=search_q) |
                                      Q(desc__icontains=search_q) )
    
    filter_post = search_post.filter(Q(title__icontains=filter_q) |
                                      Q(desc__icontains=filter_q) )
    
    paginator = Paginator(filter_post, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context['all_post'] = filter_post
    context['page_obj'] = page_obj
    
    return render(request,'index.html',context)
    
    
def create(request):
    context = dict()
    
    if request.method == "POST":
        temp_form = PostForms(request.POST)
        if temp_form.is_valid():
            clean_form = temp_form.save(commit=False)
            
            clean_form.author = User.objects.get(id = request.user.id)
            clean_form.save()
            
            return redirect('index')
        else:
            context["write_form"] = temp_form
            return render(request,'write.html',context)
    else:
        context["write_form"] = PostForms()
        return render(request,'write.html', context)
        
def detail(request,post_id):
    context = dict()
    detail_post = Post.objects.get(id = post_id)
    context['detail_post'] = detail_post
    context['comment_form'] =CommentForms()
    context['comment_all'] = Comment.objects.filter(post= Post.objects.get(id = post_id))
    return render(request,'detail.html',context)
        
def update(request,post_id):
    context = dict()
    
    if request.method == "POST":
        temp_form = PostForms(request.POST,instance=Post.objects.get(id = post_id))
        
        if temp_form.is_valid():
            temp_form.save()
            return redirect('index')
        else:
            context["write_form"] = temp_form
            return render(request,'write.html',context)
    else:
        context["write_form"] = PostForms(instance=Post.objects.get(id = post_id))
        return render(request,'write.html', context)
        
        
def delete(request,post_id):
    
    detail_post = Post.objects.get(id = post_id)
    if detail_post.author == request.user:
        detail_post.delete()
    return redirect('index')
    
def create_comment(request,post_id):
    if request.method=="POST":
        temp_form = CommentForms(request.POST)
        if temp_form.is_valid():
            clean_form = temp_form.save(commit=False)
            clean_form.post = Post.objects.get(id = post_id )
            clean_form.author = request.user
            clean_form.save()
            # temp_form.save()
            print("#"*50)
        return redirect('detail', post_id)
        
        
def comment_delete(request,post_id, com_id):
    del_com = Comment.objects.get(id=com_id)
    
    if del_com.author == request.user:
        del_com.delete()
    # else:
    #     print("작성자랑 다른 사람이 삭제하려 했씁니다.")
        
        
    return redirect('detail', post_id)

from django.http import HttpResponseRedirect

def like(request,post_id):
    like_post = Post.objects.get(id = post_id)
    
    if like_post.like.filter(username=request.user):
        like_post.like.remove(request.user)
        print("이 글의 좋아요를 취소했습니다.")
    else:
        like_post.like.add(request.user)
        print("이 글을 좋아합니다")
        
    print("좋아요를 한 사람들 : ",like_post.like.all())
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def com_like(request,com_id,post_id):
    like_com = Comment.objects.get(id = com_id)
    
    if like_com.like.filter(username=request.user):
        like_com.like.remove(request.user)
        print("이 댓글의 좋아요를 취소했습니다.")
    else:
        like_com.like.add(request.user)
        print("이 댓글을 좋아합니다")
        
    print("좋아요를 한 사람들 : ",like_com.like.all())
    
    return redirect('detail', post_id)