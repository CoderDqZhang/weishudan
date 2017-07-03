# -*- coding: utf-8 -*-

from django import forms

class AddBookForm(forms.Form):
    sbncode = forms.CharField(label="sbncode", max_length=255)
    comment = forms.CharField(label="comment", max_length=255)
    tags = forms.CharField(label="tags", max_length=255)
    uid = forms.CharField(label="uid", max_length=255)
