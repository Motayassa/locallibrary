from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)
