from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    # Метод 'all()' применён по умолчанию.
    num_roman_books = (Book.objects.filter(title__icontains='Roman') |
                       Book.objects.filter(title__icontains='Rome')).count()
    num_novel_genre = Genre.objects.filter(name__icontains='novel').count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with
    # the data in the context variable.

    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors,
                 'num_roman_books': num_roman_books,
                 'num_novel_genre': num_novel_genre,
                 'num_visits': num_visits},
        )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author

