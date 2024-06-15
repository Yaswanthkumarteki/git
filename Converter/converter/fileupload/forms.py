from django import forms
from .models import *

class FileUploadMF(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'
        widgets = {
            'file': forms.FileInput(attrs={'accept': 'video/mp4, video/webm, video/ogg'}),
        }