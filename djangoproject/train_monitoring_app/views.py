# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from djangoproject.train_monitoring_app.models import Document
from djangoproject.train_monitoring_app.forms import DocumentForm
from training_monitoring import training_monitor

from django.conf import settings

from datetime import date
import os

#Constants specifying the directory structure
UPLOAD_PATH = 'tmp'
WORK_PATH = 'gen'


def handle_uploads(request, keys):
    saved = {}
    
    upload_dir = date.today().strftime(UPLOAD_PATH)
    upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)
    
    if not os.path.exists(upload_full_path):
        os.makedirs(upload_full_path)
    
    for key in keys:
        if key in request.FILES:
            upload = request.FILES[key]
            while os.path.exists(os.path.join(upload_full_path, upload.name)):
                upload.name = '_' + upload.name
            dest = open(os.path.join(upload_full_path, upload.name), 'wb')
            for chunk in upload.chunks():
                dest.write(chunk)
            dest.close()
            saved.update({key: os.path.join(upload_dir, upload.name)})


    return saved


def show_form(request):
    # Handle file upload
    
    #Process uploaded file
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            paths= handle_uploads(request, ['docfile'])
                
            inpath = os.path.join(settings.MEDIA_ROOT, paths['docfile'])
            outpath = os.path.join(settings.MEDIA_ROOT, WORK_PATH)
            if not os.path.exists(outpath):
                os.makedirs(outpath)
            outpath = os.path.join(outpath, 'generated.pdf')
            training_monitor.create_training_stats(inpath, 0, outpath)
            os.remove(inpath)
            with open(outpath, 'r') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=test.pdf'
                os.remove(outpath)
                return response



    #Display empty
    else:
        form = DocumentForm() # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'upload_form.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
