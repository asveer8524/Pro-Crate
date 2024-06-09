from django import forms
from . import models
class post_comment(forms.ModelForm):
    class Meta:
        #file_field = forms.FileField(widget=forms.ClearableFielInput(attrs={'mulitple':True}))
        model = models.comments
        fields = ['comment_field']
