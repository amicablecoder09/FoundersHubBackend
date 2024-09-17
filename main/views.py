from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPIView(APIView):
    def get(self, request):
        data = {
            "message": "Hello, this is a test API response using APIView.",
            "status": "success",
            "data": {"key": "value"}
        }
        return Response(data)