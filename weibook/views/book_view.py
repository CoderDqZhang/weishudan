from django.http import JsonResponse
from weibook.models import book
from django.forms.models import model_to_dict
from weibook.Form import book_form
from weibook.models import book, user
from django.core.serializers import serialize
from weibook.libs import libs

def home_book_list(request):
    if request.method == 'GET':
        books_list = []
        book_list = book.Book.objects.all()
        for x in book_list:
            book_dic = model_to_dict(x,exclude=['user'])
            book_dic["user"] = model_to_dict(x.user)
            books_list.append(book_dic)
        return JsonResponse(books_list, safe=False)
    else:
        json = {"",""}
        return  JsonResponse(json)

def home_add_book(request):
    if request.method == 'POST':
        add_form = book_form.AddBookForm(request.POST)
        if add_form.is_valid():
            tmp_book = book.Book(sbncode = add_form.cleaned_data['sbncode'])
            uid = user.UserModel.objects.get(user_add_book__id = add_form.cleaned_data['uid'])
            tmp_book.uid = uid
            tmp_book.comment = add_form.cleaned_data['comment']
            tmp_book.tags = add_form.cleaned_data['tags']
            find_book = book.Book.objects.get(sbncode = add_form.cleaned_data['sbncode'], uid = user.UserModel.objects.get(user_add_book__id = add_form.cleaned_data['uid']))
            if find_book:
                print('')
                # tmp_book.objects.update()
            else:
                tmp_book.save()
            jsonData = libs.registerUrl()
            jsonData['comment'] = tmp_book.comment
            jsonData['user_tags'] = tmp_book.tags
            jsonData['user'] = model_to_dict(uid)
            return JsonResponse(jsonData)
        else:
            return JsonResponse({"false":"false_Form"})
    else:
        return JsonResponse({"false":"false_request"})