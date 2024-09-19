from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .aiArchitecture import getAIArchitecture

# Create your views here.
class GetArchitectureDiagram(APIView):
    def get(self, request):
        prompt = request.query_params.get('prompt')
        aiarchitecture = getAIArchitecture(prompt)
        data = {
            "response": aiarchitecture
            
        }
        return Response(data)
