from django import forms
from . import models
class create_project(forms.ModelForm):
    class Meta:
        #file_field = forms.FileField(widget=forms.ClearableFielInput(attrs={'mulitple':True}))
        model = models.project_data
        fields = ['title','abstract','slug','category','files']
