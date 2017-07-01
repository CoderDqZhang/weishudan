# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django import forms
from django.core import serializers
from django.core.serializers import serialize
from weibook import models
from json import dumps, loads, JSONEncoder
from django.db.models.query import QuerySet
# from django.views.decorators.csrf import csrf_protect


# Create your views here.

class LoginForm(forms.Form):
    mobile = forms.CharField(label="mobile", max_length=11)
    code = forms.CharField(label="code", max_length=50)

def loginUser(request):
    if request.method == 'POST':
        uf = LoginForm(request.POST)
        if uf.is_valid():
            mobile = uf.cleaned_data['mobile']
            print(mobile)
            code = uf.cleaned_data['code']
            print(code)
            userInfo = models.UserModel.objects.get_or_create(phone = mobile,username='',sex=1,location='',qq='',weiChat='',company='')
            print(userInfo)
            # json = dumps(models.UserModel.objects.get(phone = mobile), cls=DjangoJSONEncoder)
            json = serializers.serialize('json',[models.UserModel.objects.get(phone = mobile)],fields=('username','qq','phone'))
            # print(json)
            json = serialize('geojson',[models.UserModel.objects.get(phone = mobile)],fields=('username','qq'))
            # return HttpResponse(json)
            return JsonResponse(models.UserModel.objects.get(phone = mobile))
    else:
        json = {"",""}
        return  HttpResponse(json)

class DjangoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            # `default` must return a python serializable
            # structure, the easiest way is to load the JSON
            # string produced by `serialize` and return it
            return loads(serialize('json', obj))
        return JSONEncoder.default(self,obj)

# partial function, we can now use dumps(my_dict) instead
# of dumps(my_dict, cls=DjangoJSONEncoder)
# dumps = curry(dumps, cls=DjangoJSONEncoder)