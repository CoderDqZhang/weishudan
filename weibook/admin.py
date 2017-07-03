# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from weibook.models import user, book

# Register your models here.
admin.site.register(book.Book)
admin.site.register(user.UserModel)