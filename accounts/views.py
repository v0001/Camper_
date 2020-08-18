from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.

def signup(request):
    context=dict()
    
    if request.method=="POST":
        #회원가입 프로세스
        save_form = UserCreationForm(request.POST)
        if save_form.is_valid():
            save_form.save()
            
            ##회원가입후에 자동 로그인이 되는 프로세스
            user = authenticate(username=save_form.cleaned_data['username'], 
                                password =save_form.cleaned_data['password1'])
            
            login(request,user)
            
            return redirect('index')
        else:
            
            context['user_form'] = save_form
            return render(request,'signup.html', context)
    else:
        user_form = UserCreationForm()
        context['user_form'] = user_form
        
        
        return render(request,'registration/signup.html', context)
