from django.shortcuts import render, HttpResponse

author_info = {
    "name": "Евгений",
    "surname": "Юрченко",
    "phone": "8-900-600-10-20",
    "email": "eyurchenko@specialist.ru"
}


def main_page(request):
    result = """
    <h1>"Изучаем django!"</h1>
    <strong>Автор</strong>: <i>Юрченко Е.В.</i>
    """
    return HttpResponse(result)


def about(request):
    result = f"""
    Имя: <b>{author_info['name']}</b><br>
    Фамилия: <b>{author_info['surname']}</b><br>
    телефон: <b>{author_info['phone']}</b><br>
    email: <b>{author_info['email']}</b><br>
    """
    return HttpResponse(result)
