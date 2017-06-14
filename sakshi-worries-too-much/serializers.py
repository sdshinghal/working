from rest_framework import serializers
from .models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    """
    Serializes files added
    """
    class Meta:
        model = FileUpload
        fields = '__all__'
