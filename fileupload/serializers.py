"""Serializers"""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import File


class FileUploadSerializer(serializers.ModelSerializer):
    """
    Serializes files
    """

    class Meta:
        """
        internal
        """
        model = File
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     """Serializes users"""
#     files = serializers.PrimaryKeyRelatedField(many=True, queryset=File.objects.all())
#
#     class Meta:
#         """internal"""
#         model = User
#         fields = ('id', 'username', 'snippets')
