from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

author_info = {
    "name": "Евгений",
    "surname": "Юрченко",
    "phone": "8-900-600-10-20",
    "email": "eyurchenko@specialist.ru"
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
    {"id": 10, "name": "Новый товар", "quantity": 5},
]


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
            page = f"""
            <h1>{item['name']}</h1>
            <p> Количество: {item['quantity']} </p>
            <a href="/items">Назад</a>
            """
            return HttpResponse(page)
    return HttpResponseNotFound(f"Товар с id={id} не найден")


def items_list(request):
    context = {
        "items": items
    }
    return render(request, 'items-list.html', context)