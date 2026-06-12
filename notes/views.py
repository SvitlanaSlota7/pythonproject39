from django.shortcuts import render

def notes_view(request):
    # Тестові дані
    test_notes = [
        {"title": "План на день", "content": "Вивчити Django, повторити CSS flexbox."},
        {"title": "Покупки", "content": "Кава, фрукти, блокнот для ідей."},
        {"title": "Важливо", "content": "Здати практичне завдання вчасно!"},
    ]
    # Передаємо дані у шаблон через контекст
    return render(request, 'index.html', {'notes': test_notes})