from django import forms
from django.forms import extras
from django.utils import timezone

from .models import FileUpload


class FileUploadForm(forms.ModelForm):
    """Form to upload a file"""
    date = forms.DateField(widget=extras.SelectDateWidget, initial=timezone.now)

    class Meta:
        """internal"""
        model = FileUpload
        fields = ('name', 'owner', 'date', 'file', 'source')
