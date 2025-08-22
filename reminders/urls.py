from django.urls import path
from .views import ReminderCreateAPIView

urlpatterns = [
    path('create/', ReminderCreateAPIView.as_view(), name="create-reminder"),
]
