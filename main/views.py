from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StartupDetails, FunctionalRequirements, NonFunctionalRequirements
from .serializers import StartupDetailsSerializer, FunctionalRequirementsSerializer, NonFunctionalRequirementsSerializer

class TestAPIView(APIView):
    def get(self, request):
        data = {
            "message": "Hello, this is a test API response using APIView.",
            "status": "success",
            "data": {"key": "value"}
        }
        return Response(data)

class CreateStartupWithRequirementsAPIView(APIView):
    def post(self, request):
        # Extract startup data from the request
        startup_data = request.data.get('startup_details', None)
        functional_data = request.data.get('functional_requirements', None)
        non_functional_data = request.data.get('non_functional_requirements', None)

        # Step 1: Create StartupDetails
        if startup_data:
            startup_serializer = StartupDetailsSerializer(data=startup_data)
            if startup_serializer.is_valid():
                startup = startup_serializer.save()  # Save startup first
            else:
                return Response(startup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Startup details are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Step 2: Create FunctionalRequirements (linked to Startup)
        if functional_data:
            functional_data['startup'] = startup.id  # Set startup foreign key in functional requirements
            functional_serializer = FunctionalRequirementsSerializer(data=functional_data)
            if functional_serializer.is_valid():
                functional_serializer.save()  # Save functional requirements
            else:
                return Response(functional_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Step 3: Create NonFunctionalRequirements (linked to Startup)
        if non_functional_data:
            non_functional_data['startup'] = startup.id  # Set startup foreign key in non-functional requirements
            non_functional_serializer = NonFunctionalRequirementsSerializer(data=non_functional_data)
            if non_functional_serializer.is_valid():
                non_functional_serializer.save()  # Save non-functional requirements
            else:
                return Response(non_functional_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Step 4: Return success response after all records are created
        return Response({
            'message': 'Startup, Functional Requirements, and Non-Functional Requirements created successfully',
            'startup': StartupDetailsSerializer(startup).data  # Return created startup details
        }, status=status.HTTP_201_CREATED)


class RetrieveStartupWithRequirementsAPIView(APIView):
    def get(self, request, startup_id):
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
        response_data = {
            'startup_details': startup_serializer.data,
            'functional_requirements': functional_serializer.data,
            'non_functional_requirements': non_functional_serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)

class ListStartupsWithRequirementsAPIView(APIView):
    def get(self, request):
        # Fetch all startup details
        startups = StartupDetails.objects.all()

        # Serialize startup details
        startup_serializer = StartupDetailsSerializer(startups, many=True)

        # Prepare a list to store serialized functional and non-functional requirements
        startup_details = []

        # Iterate through each startup to fetch and serialize related requirements
        for startup in startups:
            # Fetch related functional and non-functional requirements
            functional_requirements = FunctionalRequirements.objects.filter(startup=startup)
            non_functional_requirements = NonFunctionalRequirements.objects.filter(startup=startup)

            # Serialize functional and non-functional requirements
            functional_serializer = FunctionalRequirementsSerializer(functional_requirements, many=True)
            non_functional_serializer = NonFunctionalRequirementsSerializer(non_functional_requirements, many=True)

            # Prepare startup details with related requirements
            startup_data = {
                'startup_details': startup_serializer.data,
                'functional_requirements': functional_serializer.data,
                'non_functional_requirements': non_functional_serializer.data
            }

            # Append startup details to the list
            startup_details.append(startup_data)

        return Response(startup_details, status=status.HTTP_200_OK)