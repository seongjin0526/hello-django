#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.shortcuts import redirect

def index(request):
    context = {}
    print(request.session)
    if 'email' not in request.session:
        return redirect('/login')
    else:
        email = request.session['email']

    context['email'] = email
    return render(request, 'index/index.html', context)
