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
        print(add_form)
        if add_form.is_valid():
            tmp_book = book.Book(sbncode = add_form.cleaned_data['sbncode'])
            uid = user.UserModel.objects.get(user_add_book__id = add_form.cleaned_data['uid'])
            tmp_book.uid = uid
            comment_imgs = book.Image.objects.create(url = add_form.cleaned_data['comment_imgs'])
            comment = book.Comment.objects.create(text = add_form.cleaned_data['comment_str'], uid = uid)
            comment.imgs.add(comment_imgs)
            tag = book.Tags.objects.create(tag_str = add_form.cleaned_data['tag_str'])
            find_book = book.Book.objects.get(sbncode = add_form.cleaned_data['sbncode'])
            if find_book:
                print('')
                # tmp_book.objects.update()
            else:
                tmp_book.save()
            print(comment)
            find_book.comments.add(comment)
            find_book.tags.add(tag)
            jsonData = libs.registerUrl()
            jsonData['comment'] = model_to_dict(comment, exclude='imgs')
            jsonData['comment']['imgs'] = model_to_dict(comment_imgs)

            jsonData['user_tags'] = model_to_dict(tag)
            jsonData['user'] = model_to_dict(uid)
            return JsonResponse(jsonData)
        else:
            return JsonResponse({"false":"false_Form"})
    else:
        return JsonResponse({"false":"false_request"})

