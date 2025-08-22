from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ReminderSerializer
from .services import ReminderService

class ReminderCreateAPIView(APIView):

    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                reminder = ReminderService.create_reminder(serializer.validated_data)
            except ValueError as e:  # catch service layer rule errors
                return Response(
                    {"message": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(ReminderSerializer(reminder).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)