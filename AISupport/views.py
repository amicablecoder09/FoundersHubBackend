from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import FunctionalRequirements, NonFunctionalRequirements, StartupDetails
from main.serializers import FunctionalRequirementsSerializer, NonFunctionalRequirementsSerializer, StartupDetailsSerializer

from .aiArchitecture import getAIArchitecture

# Create your views here.
class GetArchitectureDiagram(APIView):
    def get(self, request):
        prompt = request.query_params.get('prompt')
        startup_id = request.query_params.get('startup_id')
        try:
            # Fetch the startup details
            startup = StartupDetails.objects.get(id=startup_id)
        except StartupDetails.DoesNotExist:
            return Response({"error": "Startup not found"}, status=status.HTTP_404_NOT_FOUND)

        # Fetch related functional and non-functional requirements
        functional_requirements = FunctionalRequirements.objects.filter(startup=startup)
        non_functional_requirements = NonFunctionalRequirements.objects.filter(startup=startup)

        # Serialize the data
        startup_serializer = StartupDetailsSerializer(startup)
        functional_serializer = FunctionalRequirementsSerializer(functional_requirements, many=True)
        non_functional_serializer = NonFunctionalRequirementsSerializer(non_functional_requirements, many=True)

        # Prepare the response data
        startup_data = {
            'startup_details': startup_serializer.data,
            'functional_requirements': functional_serializer.data,
            'non_functional_requirements': non_functional_serializer.data
        }

        architecture = getAIArchitecture(startup_data, prompt)
        
        return Response(architecture)
