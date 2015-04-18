# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings #or from my_project import settings
import os

STORAGE_PATH ='tmp'

class Document(models.Model):
    path = os.path.join(settings.MEDIA_ROOT, STORAGE_PATH)
    docfile = models.FileField(upload_to=STORAGE_PATH)


