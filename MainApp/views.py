from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item

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


# item/1
# item/2
# item/8
# item/10
def item_page(request, id):
    for item in items:
        if item['id'] == id:
            context = {
                "item": item
            }
            # if item['quantity'] == 0:
            #     item['quantity'] = "Товара нет на складе"
            return render(request, 'item_page.html', context)
    return HttpResponseNotFound(f"Товар с id={id} не найден")


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items-list.html', context)
