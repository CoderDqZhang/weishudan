"""weishudan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from weibook.views import user_view, book_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/login/', user_view.loginUser, name='user/login'),
    url(r'^home/books_list/', book_view.home_book_list, name='home/books_list/'),
    url(r'^home/addBook/', book_view.home_add_book, name='home/addBook/')

]
