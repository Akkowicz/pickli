from django import forms

class PostForm(forms.Form):
    post_name = forms.CharField(label='Post name', max_length=128)
    content = forms.CharField(widget=forms.Textarea, max_length=5000)