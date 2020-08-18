from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from .forms import UserCreationForm, ProfileForm


# Create your views here.

def signup(request):
    context=dict()
    
    if request.method=="POST":
        #회원가입 프로세스
        save_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if save_form.is_valid():
            save_form.save()
            profile_form.save()
            ##회원가입후에 자동 로그인이 되는 프로세스
            user = authenticate(username=save_form.cleaned_data['username'], 
                                password =save_form.cleaned_data['password1'])
            
            login(request,user)
            
            tmp_profile = profile_form.save(commit = False)
            tmp_profile.save()

            return redirect('index')
        else:
            
            context['user_form'] = save_form
            return render(request,'signup.html', context)
    else:
        user_form = UserCreationForm()
        context['user_form'] = user_form
        context['profile_form'] = ProfileForm()
        
        
        return render(request,'registration/signup.html', context)
