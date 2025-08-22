from rest_framework import serializers
from .models import Reminder
from datetime import datetime

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ["id","date", "time", "message", "reminder_type"]

    def validate_date(self, value):
        today = datetime.now().date()
        if value < today:
            raise serializers.ValidationError("Cannot schedule a reminder in the past.")
        return value

    def validate(self, data):
        # If either date or time is missing (partial update), skip full datetime check
        if "date" not in data or "time" not in data:
            return data

        reminder_datetime = datetime.combine(data["date"], data["time"])
        if reminder_datetime < datetime.now():
            raise serializers.ValidationError(
                {"date": "The reminder datetime cannot be in the past."}
            )
        return data

