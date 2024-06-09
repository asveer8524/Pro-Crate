from django import forms
from . import models

class addProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['name','email','mobile_no','profile_pic','city','department', 'type']
