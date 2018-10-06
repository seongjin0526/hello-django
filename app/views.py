#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections

def sample(request):
    sample_list = [1,2,3,4]
    print(sample_list)
    context = {}
    context['sample_list'] = sample_list
    return render(request, 'app/templates/sample.html', context)
