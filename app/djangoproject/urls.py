# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
	(r'^train_monitoring_app/', include('djangoproject.train_monitoring_app.urls')),
	(r'^$', RedirectView.as_view(url='/train_monitoring_app/upload/')), # Just for ease of use.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
