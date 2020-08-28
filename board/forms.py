from django.forms import ModelForm
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget


class PostForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'mytitle',
            'autocomplete': 'off',
            'placeholder': '제목을 입력해주세요'
        })
        self.fields['desc'].widget.attrs.update({

            'autocomplete': 'off',
            'placeholder': '내용을 입력해주세요'
        })

        # self.fields['comment'].widget.attrs.update(size='40')

    class Meta:
        model = Post
        # fields = [ 'title', 'desc']
        fields = [ 'title', 'desc', 'camp_type', 
        'address','position_latitude','position_longitude',
        'facility_toilet','facility_showerroom','facility_cookroom',
        'facility_store','facility_electric','facility_water_sewage','facility_fire',
        'capacity','price_min','price_max']
        #'__all__'
        
        widgets = {'desc': SummernoteWidget()}

# class PostForms2(ModelForm):
#     class Meta:
#         model = Post
#         fields = [ 'camp_type']
        
#         # CHOICES=[('백패킹','back'),
#         #          ('차박','car'),
#         #          ('오토캠핑','auto')]

#         # like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

# class PostForms3(ModelForm):
#     class Meta:
#         model = Post
#         fields = [ 'address','position_latitude','position_longitude',
#         'facility_toilet','facility_showerroom','facility_cookroom',
#         'facility_store','facility_electric','facility_water_sewage','facility_fire',
#         'capacity','price_min','price_max']

class CommentForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs.update({
            'autocomplete': 'off',
            'placeholder': '댓글을 입력해주세요'
        })

    class Meta:
        model = Comment
        fields = ("desc", )
