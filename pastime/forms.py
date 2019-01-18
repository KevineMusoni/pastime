from django import forms

from .models import *

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget=forms.TextInput()
    class Meta:
        model = Profile
        # userprofile arguments 
        fields = ('Name','profile_picture','bio','age')