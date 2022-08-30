from django.urls import path

from reminder_celery.views import contact_us, index, message_sent, reminder_set


app_name = 'reminder'
urlpatterns = [
    path('', index, name='index'),
    path('reminderset/', reminder_set, name='reminder-set'),
    path('contact_us/', contact_us, name='contact-us'),
    path('message_sent/', message_sent, name='message-sent'),
]
