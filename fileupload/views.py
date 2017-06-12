"""View File"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import File
from .serializers import FileUploadSerializer
from .forms import FileUploadForm
from .permissions import IsGroupOrReadOnly


class FileUploadView(APIView):
    """File Upload methods"""
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsGroupOrReadOnly]

    def put(self, request):
        """
        Update file if required
        :param request:
        :return:
        """
        if request.user.is_staff or not request.user.is_superuser:
            file_obj = request.data['file']

            return Response(status=204)

    def get(self, request):
        """
        Create upload form instance
        :param request:
        :return:
        """
        form = FileUploadForm()
        return render(request, "fileupload/fileupload.html", {"form": form})

    def post(self, request):
        """
        Save uploaded file to databases
        :param request:
        :return:
        """

        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.save()
            return redirect('ListFile')


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Details of file
    """
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer


class ListFile(generics.ListCreateAPIView):
    """
    List showing entire file
    """
    permission_classes = [IsAuthenticated]
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
