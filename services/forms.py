from django import forms
from users.models import Profile

class ProfileForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Profile
        fields = ['picture', 'phone_number', 'street', 'city', 'state', 'zip_code']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = ""

    

class UpdateProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    phone_number = forms.CharField(max_length=25)
    street = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=10)
    
    class Meta:
        model = Profile
        fields = ['picture', 'phone_number', 'street', 'city', 'state', 'zip_code']