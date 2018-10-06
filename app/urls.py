from django.urls import path
from django.conf.urls import url
from . import views

from .djangoapps.login import views as LoginViews
from .djangoapps.logout import views as LogoutViews
from .djangoapps.index import views as IndexViews
from .djangoapps.regist import views as RegistViews

urlpatterns = [
    # main-url
    url('sample$', views.sample, name='sample'),
    url('api_login$', LoginViews.api_login, name='api_login'),
    url('login$', LoginViews.login, name='login'),
    url('api_logout$', LogoutViews.api_logout, name='api_logout'),

    url('api_regist$', RegistViews.api_regist, name='api_regist'),
    url('regist$', RegistViews.regist, name='regist'),
    url('$', IndexViews.index, name='index'),

]
