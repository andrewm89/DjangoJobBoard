from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import availablejobs as Jobs

# Create your views here.
def showjobs(request):
    context = {}
    context['jobs'] = Jobs.objects.all()
    html = TemplateResponse(request,'jobs.html',context)
    return HttpResponse(html.render())
