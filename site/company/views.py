from django.shortcuts import render

from .models import Category, Tovar, Page
# Create your views here.

def index(request):
    date = {
    "title" : "Главная страница",
    "category": Category.objects.all(),
    "pages": Page.objects.all(),
    "tovar": Tovar.objects.all()[:20],
    "page_id": 1 ,
    }
    return render(request, "index.html", date)

def error(request):
    return render(request, "my404.html", { 'title': 'Ошибка нет такой страницы'})

def contact(request):
    page = Page.objects.get(slug = request.path.strip('/'))
    date = {
    "title" : page.name,
    "category": Category.objects.all(),
    "pages": Page.objects.all(),
    "page_id": page.id ,
    }
    return render(request, "contact.html", date)

def company(request):
    page = Page.objects.get(slug = request.path.strip('/'))
    date = {
    "title" : page.name,
    "category": Category.objects.all(),
    "pages": Page.objects.all(),
    "page_id": page.id ,
    }
    return render(request, "company.html", date)

def catalog(request):
    page = Page.objects.get(slug = request.path.strip('/'))
    date = {
    "title" : page.name,
    "category": Category.objects.all(),
    "pages": Page.objects.all(),
    "page_id": page.id ,
    }
    return render(request, "catalog.html", date)

def category(request, cat_slug):
    # page = Page.objects.get(slug = request.path.strip('/'))
    category = Category.objects.get(slug = cat_slug)
    
    date = {
    "title" : category,
    "category": Category.objects.all(),
    "tovar": Tovar.objects.filter(category=category),
    "pages": Page.objects.all(),
    "page_id": 4 ,
    }
    return render(request, "category.html", date)

def tovar(request, cat_slug, tov_slug):
    pass
    # return render(request, {"tovar": tov_slug})

def custom_500(request):
    # print("Проверка")
    response = render(request, '500.html', {})
    response.status_code = 404
    return response