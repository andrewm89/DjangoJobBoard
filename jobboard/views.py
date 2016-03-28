from django.http import HttpResponse
from django.template.response import TemplateResponse

def index(request):
    context = {}
    html = TemplateResponse(request,'welcome.html',context)
    return HttpResponse(html.render())
