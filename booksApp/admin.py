from django.contrib import admin

from booksApp.models import Book, Publisher

# Register your models here.

admin.site.register(Book)
admin.site.register(Publisher)

