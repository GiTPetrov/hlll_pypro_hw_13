from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class ReminderForm(forms.Form):
    email = forms.EmailField(label='Reminder email')
    reminder_text = forms.CharField(label='Reminder text')
    schedule = forms.DateTimeField(label='Reminder date and time')

    def clean_schedule(self):
        now = timezone.now()
        clnd_schedule = self.cleaned_data['schedule']
        diff_days = now - clnd_schedule
        if diff_days.days <= -3 or diff_days.days >= 0:
            raise ValidationError("The reminder date shouldn't be less than today and more than two days forward")
        return clnd_schedule


class ContactForm(forms.Form):
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Name')
    message_text = forms.CharField(label='Message text')
