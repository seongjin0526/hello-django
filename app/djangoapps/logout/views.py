#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def api_logout(request):
    del request.session['email']
    return JsonResponse({'result':'success'})