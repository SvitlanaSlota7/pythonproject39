from django.contrib import admin
from django.urls import path
from notes.views import notes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notes_view, name='home'), # Головна сторінка
]
