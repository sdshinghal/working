"""Models"""
from django.db import models
from django.conf import settings

SOURCE_CHOICES = {
    ('adwords', 'AdWords'),
    ('taboola', 'Taboola'),
    ('outbrain', 'Outbrain'),
    ('timesinternet', 'Times Internet')
}


class File(models.Model):
    """Upload files"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(choices=SOURCE_CHOICES, default='adwords', max_length=100)

    def __str__(self):
        return str(self.name)
