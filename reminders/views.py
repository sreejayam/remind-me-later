from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import ReminderSerializer
from .services import ReminderService

class ReminderCreateAPIView(APIView):

    def get(self, request):
        reminders = Reminder.objects.all().order_by("-date", "-time")
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                reminder = ReminderService.create_reminder(serializer.validated_data)
            except ValueError as e:
                return Response(
                    {"message": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(ReminderSerializer(reminder).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            reminder = Reminder.objects.get(pk=pk)
        except Reminder.DoesNotExist:
            return Response({"error": "Reminder not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReminderSerializer(reminder, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            reminder = Reminder.objects.get(pk=pk)
        except Reminder.DoesNotExist:
            return Response({"error": "Reminder not found"}, status=status.HTTP_404_NOT_FOUND)

        reminder.delete()
        return Response({"message": "Reminder deleted successfully"}, status=status.HTTP_204_NO_CONTENT)