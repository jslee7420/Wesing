from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields= ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 써주세요.'}),
            'text': forms.Textarea(
                attrs={'placeholder': '내용을 써주세요.'}),
        }
