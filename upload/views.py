from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from . import processing
import json

# Create your views here.

def upload(request):
    template = loader.get_template('upload/upload.html')
    if request.method=='POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save('uploaded_file.xlsx', uploaded_file)
    return HttpResponse(template.render([],request))

def filter_compound(request):
    processor_object = processing.Processor('./media/uploaded_file.xlsx')
    processor_object.filter_compound_id()
    return HttpResponse("<a href = '../media/output_lpc.xlsx'>download lpc output file</a><br><a href = '../media/output_pc.xlsx'>download pc output file</a><br><a href = '../media/output_plasmalogen.xlsx'>download plasmalogen output file</a>")


def round_time(request):
    processor_object = processing.Processor('./media/uploaded_file.xlsx')
    processor_object.round_retention_time()
    return HttpResponse("<a href = '../media/output_rounded.xlsx'>download rounded output file</a>")

def mean_finder(request):
    processor_object = processing.Processor('./media/uploaded_file.xlsx')
    processor_object.group_mean_finder()
    return HttpResponse("<a href = '../media/output_mean.xlsx'>download mean file</a>")