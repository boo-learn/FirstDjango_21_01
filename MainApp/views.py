from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

author_info = {
    "name": "Евгений",
    "surname": "Юрченко",
    "phone": "8-900-600-10-20",
    "email": "eyurchenko@specialist.ru"
}


def main_page(request):
    return render(request, 'index.html')


def about(request):
    context = {
        "author": author_info
    }
    return render(request, 'about.html', context)


def item_page(request, id):
    try:
        item = Item.objects.get(pk=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id={id} не найден")
    context = {
        "item": item
    }
    return render(request, 'item_page.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items-list.html', context)
