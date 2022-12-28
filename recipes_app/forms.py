from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Create a Comment Form
    """
    class Meta:
        model = Comment
        fields = ('body',)
