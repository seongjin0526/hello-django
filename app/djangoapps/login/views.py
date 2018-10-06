#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.db import connections

def login(request):
    context = {}
    return render(request, 'login/login.html', context)


def api_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    print(email, password)

    with connections['default'].cursor() as cur:
        query = '''
                select count(*)
                FROM user where name='{email}' and password='{password}'
            '''.format(email=email, password=password)
        print(query)
        cur.execute(query)
        rows = cur.fetchall()
        print(rows)

    if rows[0][0] != 0:
        request.session['email'] = email
        return JsonResponse({'result':'success'}) #session up

    return JsonResponse({'result':'false'})