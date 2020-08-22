from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, ProfileForm
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    context = dict()

    if request.method == "POST":
        #회원가입 프로세스
        save_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        print('save_form',save_form)
        
        print('profile_form',profile_form)
        

        if save_form.is_valid() and profile_form.is_valid():
            save_form.save()

            ##회원가입후에 자동 로그인이 되는 프로세스
            user = authenticate(username=save_form.cleaned_data['username'],
                                password=save_form.cleaned_data['password1'])

            login(request, user)

            get_profile = Profile.objects.get(id=user.profile.id)

            get_profile.nickname = profile_form.cleaned_data['nickname']
            get_profile.location = profile_form.cleaned_data['location']
            get_profile.age = profile_form.cleaned_data['age']

            # tmp_profile = profile_form.save(commit=False)
            # tmp_profile.user = user #authenticate 성공한 user를 바로넣자
            get_profile.save()

            return redirect('index')
        else:

            context['user_form'] = save_form
            return render(request, 'registration/signup.html', context)
    else:
        user_form = UserCreationForm()
        context['user_form'] = user_form
        # profile_form = ProfileForm()
        context['profile_form'] = ProfileForm()
        return render(request, 'registration/signup.html', context)


def profile(request, pk):
    context = dict()
    pro_info = User.objects.get(id=pk)
    context['pro_info'] = pro_info
    return render(request, 'profile.html', context)
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, ProfileForm
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    context = dict()

    if request.method == "POST":
        #회원가입 프로세스
        save_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if save_form.is_valid() and profile_form.is_valid():
            save_form.save()

            ##회원가입후에 자동 로그인이 되는 프로세스
            user = authenticate(username=save_form.cleaned_data['username'],
                                password=save_form.cleaned_data['password1'])

            login(request, user)

            get_profile = Profile.objects.get(id=user.profile.id)

            get_profile.nickname = profile_form.cleaned_data['nickname']
            get_profile.location = profile_form.cleaned_data['location']
            get_profile.age = profile_form.cleaned_data['age']

            # tmp_profile = profile_form.save(commit=False)
            # tmp_profile.user = user #authenticate 성공한 user를 바로넣자
            get_profile.save()

            return redirect('index')
        else:

            context['user_form'] = save_form
            return render(request, 'signup.html', context)
    else:
        user_form = UserCreationForm()
        context['user_form'] = user_form
        # profile_form = ProfileForm()
        context['profile_form'] = ProfileForm()
        return render(request, 'registration/signup.html', context)


def profile(request, pk):
    context = dict()
    pro_info = User.objects.get(id=pk)
    context['pro_info'] = pro_info
    return render(request, 'profile.html', context)
