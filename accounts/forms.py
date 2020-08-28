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


# class ProfileForm(forms.ModelForm):
loc_choices = (
        ('37.5609532,126.9789455', '서울'),
        ('35.1797957,129.0727983', '부산'),
        ('35.8692985,128.5372972', '대구'),
        ('37.4568565,126.7029735', '인천'),
        ('35.1608052,126.8325019', '광주'),
        ('36.350461,127.38263', '대전'),
        ('35.5170365,129.126154', '울산'),
        ('37.2750552,127.0072561', '경기도'),
        ('37.8853984,127.7122663', '강원도'),
        ('36.6358136,127.4891451', '충청북도'),
        ('36.6588327,126.6706662', '충청남도'),
        ('35.8203643,127.1065383', '전라북도'),
        ('34.816223,126.4607355', '전라남도'),
        ('36.576025,128.5034069', '경상북도'),
        ('35.2382949,128.6902093', '경상남도'),
        ('33.499597,126.5268766', '제주'),
    )


class ProfileForm(forms.ModelForm):

    location = forms.ChoiceField(choices=loc_choices)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].label = "관심지역"
    class Meta:
        model = mypage
        fields = ("location", "age")
