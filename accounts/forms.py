from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import mypage


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update(
    #         {'required': 'True',
    #         'placeholder':'댓글을 입력해주세요,'
    #     })
# def save(self, commit=True):
#     user = super(UserCreationForm, self).save(commit=False)
#     user.email = self.cleaned_data["email"]
#     if commit:
#         user.save()
#     return user


class ProfileForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['desc'].widget.attrs.update(
    #         {'autocomplete': 'off',
    #         'placeholder':'댓글을 입력해주세요,'
    #         })

    class Meta:
        model = mypage
        fields = ("location", "age")
