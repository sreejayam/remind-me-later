from django.urls import reverse
from rest_framework.test import APITestCase
from datetime import date, timedelta

class ReminderAPITest(APITestCase):
    def setUp(self):
        self.url = reverse("create-reminder")

    def test_create_valid_reminder(self):
        payload = {
            "date": (date.today() + timedelta(days=1)).isoformat(),
            "time": "10:00:00",
            "message": "A meeting tomorrow at 10 am",
            "reminder_type": "Email",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["message"], "A meeting tomorrow at 10 am")
        self.assertEqual(response.data["reminder_type"], "Email")

    def test_reject_past_reminder(self):
        payload = {
            "date": (date.today() - timedelta(days=1)).isoformat(),
            "time": "09:00:00",
            "message": "Old reminder",
            "reminder_type": "SMS",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Cannot schedule a reminder in the past", str(response.data))
    def test_reject_invalid_reminder_type(self):
        payload = {
            "date": (date.today() + timedelta(days=1)).isoformat(),
            "time": "09:00:00",
            "message": "Invalid type test",
            "reminder_type": "PushNotification",  # not allowed
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("is not a valid choice", str(response.data))

    def test_reject_empty_message(self):
        payload = {
            "date": (date.today() + timedelta(days=1)).isoformat(),
            "time": "09:00:00",
            "message": "",  # serializer handle it
            "reminder_type": "SMS",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("may not be blank", str(response.data))


