from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
def calculator(request):
    template = loader.get_template('calc.html')
    return HttpResponse(template.render())

