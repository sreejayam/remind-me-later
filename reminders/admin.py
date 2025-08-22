from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "time", "reminder_type", "message", "created_at")
    list_filter = ("reminder_type", "date")
