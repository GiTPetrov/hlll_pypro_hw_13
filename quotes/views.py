from django.shortcuts import get_object_or_404, render

from quotes.models import Quote, QuoteAuthor


def author_info(request, pk):
    author = get_object_or_404(QuoteAuthor, pk=pk)
    return render(request, 'quotes/author_info.html', {'author_info': author})


def authors_list(request):
    authors_queryset = QuoteAuthor.objects.all()
    return render(request, 'quotes/authors_list.html', {'authors': authors_queryset})


def authors_quotes(request, pk):
    author = get_object_or_404(QuoteAuthor, pk=pk)
    quotes = author.quote_set.all()
    return render(request, 'quotes/authors_quotes.html', {'author': author, 'quotes': quotes})


def quotes_index(request):
    return render(request, 'quotes/index.html',)


def quotes_list(request):
    quotes_queryset = Quote.objects.select_related('quote_author').all()
    return render(request, 'quotes/quotes_list.html', {'quotes': quotes_queryset})
