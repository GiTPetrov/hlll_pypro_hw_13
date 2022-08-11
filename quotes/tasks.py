from datetime import datetime

from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

from quotes.models import Quote, QuoteAuthor

import requests


@shared_task
def parce_quotes():
    url = 'https://quotes.toscrape.com'
    quotes_page = requests.get(url)
    structure = BeautifulSoup(quotes_page.content, features='html.parser')
    quote = structure.find_all('div', {'class': 'quote'})
    quote_counter_limit = 8
    quote_counter = 0

    while True:
        for item in quote:
            while quote_counter < quote_counter_limit:
                quote_text = item.span.text.strip('“”')
                quote_author = item.small.text
                quote_obj, quote_created = Quote.objects.get_or_create(
                    quote_text=quote_text,
                )
                if quote_created is True:
                    author_url = f'{url}{item.a.get("href")}'
                    author_page = requests.get(author_url)
                    author_structure = BeautifulSoup(author_page.content, features='html.parser')
                    author_details = author_structure.find('div', {'class': 'author-details'})
                    author_birthdate = author_details.find_all("span")[0].text
                    pd = datetime.date(datetime.strptime(author_birthdate, "%B %d, %Y"))
                    author_birthplace = author_details.find_all("span")[1].text.replace('in ', '')
                    ad = author_details.div.text
                    author_description = ad.strip()
                    author_obj, author_created = QuoteAuthor.objects.get_or_create(
                        author_name=quote_author,
                        defaults={
                            'author_birthdate': pd,
                            'author_birthplace': author_birthplace,
                            'author_description': author_description,
                        },
                    )
                    author_obj.quote_set.add(quote_obj)
                    quote_counter += 1
                break
        pagination_search = structure.find('li', {'class', 'next'})
        if quote_counter == quote_counter_limit:
            send_mail(
                'End of quote counter!',
                f'Was imported {quote_counter_limit} new quotes',
                'superuser_email@ukr.net',
                ['quote_admin@ukr.net', ],
                fail_silently=False,
            )
            break
        elif bool(pagination_search) is False:
            send_mail(
                'End of pagination!',
                'All pages was parsed',
                'superuser_email@ukr.net',
                ['quote_admin@ukr.net', ],
                fail_silently=False,
            )
            break
        pagination_url = f"{url}{pagination_search.a.get('href')}"
        quotes_page = requests.get(pagination_url)
        structure = BeautifulSoup(quotes_page.content, features='html.parser')
        quote = structure.find_all('div', {'class': 'quote'})
