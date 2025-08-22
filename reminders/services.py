from datetime import datetime
from typing import Dict, Any
from django.utils import timezone
from django.db import transaction
from .models import Reminder

class ReminderService:


    @staticmethod
    def _combine_to_aware_datetime(date, time_):
        scheduled_naive = datetime.combine(date, time_)
        return timezone.make_aware(scheduled_naive, timezone.get_current_timezone())

    @staticmethod
    def _validate_business_rules(data: Dict[str, Any]) -> None:
        scheduled_at = ReminderService._combine_to_aware_datetime(data["date"], data["time"])
        if scheduled_at < timezone.now():
            raise ValueError("Cannot schedule a reminder in the past.")

        if data["reminder_type"] not in ("SMS", "Email"):
            raise ValueError("Unsupported reminder type.")

        msg = (data.get("message") or "").strip()
        if not msg:
            raise ValueError("Message cannot be empty.")

    @staticmethod
    @transaction.atomic
    def create_reminder(validated_data: Dict[str, Any]) -> Reminder:
        ReminderService._validate_business_rules(validated_data)
        reminder = Reminder.objects.create(**validated_data)
        return reminder

# TODO: Integrate Celery beat to trigger sending reminders at scheduled time
