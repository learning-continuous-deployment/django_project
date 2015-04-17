# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('djangoproject.train_monitoring_app.views',
    url(r'^upload/$', 'show_form', name='upload'),
)
