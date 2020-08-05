from django import forms
from .models import Question, Post

class NewQuestion(forms.ModelForm):
    ans = forms.CharField(
        widget = forms.Textarea(attrs={
            'rows' : 5, 'placeholder' : 'Enter your answer...'
        }),
         max_length = 4000,
         help_text = "Max length of the answer is 4000"
         )
    
    class Meta:
        model = Question
        fields = ['ques', 'ans']

class PostAns(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['ans']