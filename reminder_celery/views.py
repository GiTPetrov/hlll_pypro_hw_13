from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils import timezone

from reminder_celery.forms import ContactForm, ReminderForm
from reminder_celery.tasks import reminder_schedule, contact_form


def index(request):
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
        }
    )


def reminder_set(request):
    return render(request, 'reminder_celery/reminder_set.html')


def contact_us_form(request, form, template_name):
    data = dict()
    if 'send_mail' in request.GET:
        if form.is_valid():
            clnd_email = form.cleaned_data["email"]
            clnd_name = form.cleaned_data["name"]
            clnd_message_text = form.cleaned_data["message_text"]
            contact_form.apply_async((clnd_email, clnd_name, clnd_message_text),)
            data['form_is_valid'] = True
            data['form_sent'] = render_to_string('reminder_celery/includes/partial_form_sent.html', )
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def contact_us(request):
    if 'send_mail' in request.GET:
        form = ContactForm(request.GET)
    else:
        form = ContactForm()
    return contact_us_form(request, form, 'reminder_celery/includes/partial_contact_new.html')


def message_sent(request):
    if 'send_mail' in request.GET:
        form = ContactForm(request.GET)
    else:
        form = ContactForm()
    return contact_us_form(request, form, 'reminder_celery/includes/partial_contact_new.html')
