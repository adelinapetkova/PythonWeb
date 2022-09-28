from django.contrib import admin

from expences_tracker.expenses_tracker.models import Profile, Expense

admin.site.register(Profile)
admin.site.register(Expense)
