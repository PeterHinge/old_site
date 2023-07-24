from django import forms
from .models import Comment


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_name', 'user_email', 'content')
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'user_email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
