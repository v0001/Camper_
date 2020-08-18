from django.forms import ModelForm
from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget



class PostForms(ModelForm):
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'mytitle',
            'autocomplete': 'off',
            'placeholder':'제목을 입력해주세요,'
            })
        self.fields['desc'].widget.attrs.update(
            {'class': 'mydesc',
            'autocomplete': 'off',
            'placeholder':'내용을 입력해주세요'
            })
        # self.fields['comment'].widget.attrs.update(size='40')
    
    class Meta:
        model = Post
        fields = ('title',"desc",)
        widgets = {
            'desc': SummernoteWidget()
        }
    
class CommentForms(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs.update(
            {'autocomplete': 'off',
            'placeholder':'댓글을 입력해주세요,'
            })
        
    class Meta:
        model = Comment
        fields = ("desc",)