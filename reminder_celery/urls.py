from django.urls import path

from reminder_celery.views import index, reminder_set


app_name = 'reminder'
urlpatterns = [
    path('', index, name='index'),
    path('reminderset/', reminder_set, name='reminder-set'),
]
