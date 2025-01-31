from django import forms
from .models import Post 



class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": ""}))
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = ""






# class UpdatePostForm(forms.ModelForm):
#     title = forms.CharField(max_length=200)
#     image = forms.ImageField()
#     content = forms.CharField(widget=forms.Textarea)

#     class Meta:
#         model = Post
#         fields = ['title', 'image', 'content']

    