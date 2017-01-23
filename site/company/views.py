from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Category, Tovar, Page
# Create your views here.


def index(request):
    date = {
            "title": "Главная страница",
            "category": Category.objects.all(),
            "pages": Page.objects.all(),
            "tovar": Tovar.objects.all()[:20],
            "page_id": 1,
            }
    return render(request, "index.html", date)


def contact(request):
    page = Page.objects.get(slug=request.path.strip('/'))
    date = {
            "title": page.name,
            "category": Category.objects.all(),
            "pages": Page.objects.all(),
            "page_id": page.id,
    }
    return render(request, "contact.html", date)


def company(request):
    page = Page.objects.get(slug=request.path.strip('/'))
    date = {
        "title": page.name,
        "category": Category.objects.all(),
        "pages": Page.objects.all(),
        "page_id": page.id,
    }
    return render(request, "company.html", date)


def catalog(request):
    page = Page.objects.get(slug=request.path.strip('/'))
    date = {
        "title": page.name,
        "category": Category.objects.all(),
        "pages": Page.objects.all(),
        "page_id": page.id,
    }
    return render(request, "catalog.html", date)


def category(request, cat_slug):
    # page = Page.objects.get(slug = request.path.strip('/'))
    category = Category.objects.get(slug=cat_slug)
    # print(category)
    date = {
        "title": category,
        "category": Category.objects.all(),
        "tovar": Tovar.objects.filter(category=category),
        "pages": Page.objects.all(),
        "page_id": 4,
    }
    return render(request, "category.html", date)


def tovar(request, cat_slug, tov_slug):
    tovar = Tovar.objects.get(slug=tov_slug)
    date = {
        "title": '{} {}'.format(str(tovar), 'от компании СВАОР'),
        "category": Category.objects.all(),
        "tovar": tovar,
        "pages": Page.objects.all(),
        "page_id": 4,
    }
    return render(request, "tovar.html", date)


def zakaz(request):
    from django.conf import settings
    from django.core.mail import send_mail
    my_post = request.POST
    print(my_post)
    my_send = "Товар: {}\nАвтор: {}\nТелефон: {}\nСообщение:{}".format(my_post['zakaz'], my_post['author'], my_post['phone'], my_post['text'])
    send_mail('Заказ товара', my_send, settings.EMAIL_HOST_USER, ['89507850000s@gmail.com'], fail_silently=False)
    return HttpResponse("")
