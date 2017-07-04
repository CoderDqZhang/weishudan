# -*- coding: utf-8 -*-

from django import forms

class AddBookForm(forms.Form):
    sbncode = forms.CharField(label="sbncode", max_length=255)
    comment_str = forms.CharField(label="comment_str", max_length=255)
    comment_imgs = forms.CharField(label='comment_imgs', max_length=255)
    tag_str = forms.CharField(label="tag_str", max_length=255)
    uid = forms.CharField(label="uid", max_length=255)
