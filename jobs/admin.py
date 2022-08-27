from django.contrib import admin

# Register your models here.
from .models import Job, MailingListPerson

admin.site.register(Job)
admin.site.register(MailingListPerson)
