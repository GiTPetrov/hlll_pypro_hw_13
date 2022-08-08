from django.shortcuts import redirect, render
from django.utils import timezone

from reminder_celery.forms import ReminderForm
from reminder_celery.tasks import reminder_schedule


def index(request):
    hypo = None
    if 'reminde_me' in request.GET:
        form = ReminderForm(request.GET)
        if form.is_valid():
            clnd_email = form.cleaned_data["email"]
            clnd_reminder_text = form.cleaned_data["reminder_text"]
            clnd_schedule = form.cleaned_data["schedule"]
            reminder_schedule.apply_async((clnd_email, clnd_reminder_text), eta=clnd_schedule)

            return redirect('reminder:reminder-set')
    else:
        form = ReminderForm(initial={'schedule': timezone.now()})
    return render(
        request,
        'reminder_celery/index.html',
        {
            'get_rmndr_form': form,
            'hypothesis': hypo,
        }
    )


def reminder_set(request):
    return render(request, 'reminder_celery/reminder_set.html')
