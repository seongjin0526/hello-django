#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections

def regist(request):
    print("qwer")
    context = {}
    return render(request, 'regist/regist.html', context)

def api_regist(request):
    print('asdf')
    context = {}

    email = request.POST.get('email')
    password = request.POST.get('password')

    print(email, password)

    with connections['default'].cursor() as cur:
        query = '''
              insert into user (name, password) values ('{email}', '{password}');            
              '''.format(email=email, password=password)
        cur.execute(query)

    return JsonResponse({'result':'success'})
