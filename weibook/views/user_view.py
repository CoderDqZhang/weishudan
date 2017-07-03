# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django import forms
from django.core import serializers
from django.core.serializers import serialize
from weibook.models import user
from json import dumps, loads, JSONEncoder
from django.db.models.query import QuerySet
from django.forms.models import model_to_dict


# Create your views here.

class LoginForm(forms.Form):
    mobile = forms.CharField(label="mobile", max_length=11)
    code = forms.CharField(label="code", max_length=50)

def loginUser(request):
    if request.method == 'POST':
        uf = LoginForm(request.POST)
        if uf.is_valid():
            mobile = uf.cleaned_data['mobile']
            code = uf.cleaned_data['code']
            userInfo = user.UserModel.objects.get_or_create(phone = mobile)
            return JsonResponse(model_to_dict(user.UserModel.objects.get(phone = mobile)))
    else:
        json = {"",""}
        return  HttpResponse(json)