from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from campaign_analysis.views import trigger_campaign_data_fetch, FileUploadView


urlpatterns = [
    url(r'^trigger$', trigger_campaign_data_fetch),
    url(r'^upload/$', FileUploadView.as_view()),
    url(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
