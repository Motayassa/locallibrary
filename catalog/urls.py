from django.urls import path
from . import views


urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^books/$', views.BookListView.as_view(), name='books'),
]
