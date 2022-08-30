from celery import shared_task

from django.core.mail import send_mail


@shared_task
def reminder_schedule(email, text):
    send_mail(
        'Reminder',
        text,
        'superuser_email@ukr.net',
        [email, ],
        fail_silently=False,
    )


@shared_task
def contact_form(email, name, text):
    send_mail(
        f'{name}. Request from contact form',
        text,
        email,
        ['superuser_email@ukr.net', ],
        fail_silently=False,
    )
