from campaign_analysis.forms import FileUploadForm
from campaign_analysis.serializers import FileUploadSerializer
from campaign_analysis.lib.parsers import Adwords, Outbrain, Taboola, TimesInternet
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from campaign_analysis.permissions import IsGroupOrReadOnly
from django.shortcuts import render, redirect
from django.http import Http404
from campaign_analysis.tasks import fetch_piwik_data
import logging
from campaign_analysis.utils import generate_date
logging.basicConfig(level=20)


@api_view(['GET'])
def trigger_campaign_data_fetch(request):
    """
     Triggers task to fetch data from Piwik
    :param request: DRF request object
    :return: DRF response object containing output of the action
    """
    try:
        date_records = generate_date()
        for date in date_records:
            fetch_piwik_data.delay(date)
        return Response("Job triggered successfully!")
    except Exception as e:
        logging.error("Exception: {}".format(str(e)))
        return Response("Error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FileUploadView(APIView):
    """
    Creates, updates and saves files to be uploaded
    """
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsGroupOrReadOnly]

    def get(self, request):
        """
        Creates upload form for user to fill in
        :param request: DRF GET request object
        :return: DRF response object containing output of the action
        """
        form = FileUploadForm()
        return render(request, "campaign_analysis/file_upload.html", {"form": form})

    def put(self, request):
        """
        Updates uploaded file
        :param request: DRF PUT request object
        :param pk: pk of object being requested
        :return: DRF response object containing output of the action
        """

        file_obj = request.data['file']
        serializer = FileUploadSerializer(file_obj)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def process_file(self, file_obj):
        sources = {Adwords: "adwords",
                   Taboola: "taboola",
                   Outbrain: "outbrain",
                   TimesInternet: "timesinternet"}
        for option in sources:
            if str(file_obj.source) == sources[option]:
                option.process_records(file_obj)

    def post(self, request):
        """
        Saves user-uploaded file and populates database based on given source
        :param request: DRF POST request object
        :return: DRF response object (redirect to view trigger)
        """
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = form.save(commit=False)
            self.process_file(file_obj)
            file_obj.save()
            return redirect('trigger')

    def delete(self, request):
        """
        Deletes file requested
        :param request: DRF DELETE request object
        :param pk: pk of object being requested
        :return: DRF response object (redirect to view trigger)
        """
        file_obj = request.data['file']
        file_obj.delete()
        return redirect('trigger')
