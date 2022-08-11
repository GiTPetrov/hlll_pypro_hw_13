from django.urls import path

from quotes.views import author_info, authors_list, authors_quotes, quotes_index, quotes_list


app_name = 'quotes'
urlpatterns = [
    path('', quotes_index, name='index'),
    path('authorslist/', authors_list, name='authors-list'),
    path('authorinfo/<int:pk>/', author_info, name='author-info'),
    path('authorinfo/<int:pk>/quotes', authors_quotes, name='authors-quotes'),
    path('quoteslist/', quotes_list, name='quotes-list'),
]
