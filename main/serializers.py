from rest_framework import serializers
from .models import StartupDetails, FunctionalRequirements, NonFunctionalRequirements

# Serializer for StartupDetails model
class StartupDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupDetails
        fields = [
            'id', 
            'startup_name', 
            'founder_name', 
            'contact_email', 
            'startup_stage', 
            'funding_status', 
            'number_of_employees'
        ]

# Serializer for FunctionalRequirements model
class FunctionalRequirementsSerializer(serializers.ModelSerializer):
    # StartupDetails is a foreign key, linking FunctionalRequirements to StartupDetails
    startup = serializers.PrimaryKeyRelatedField(queryset=StartupDetails.objects.all(), required=True)

    class Meta:
        model = FunctionalRequirements
        fields = [
            'id', 
            'startup',  # This will hold the foreign key to StartupDetails
            'business_domain', 
            'application_features', 
            'user_interface', 
            'data_management', 
            'expected_number_of_users', 
            'expected_number_of_transactions', 
            'cloud_provider', 
            'deployment_model'
        ]

# Serializer for NonFunctionalRequirements model
class NonFunctionalRequirementsSerializer(serializers.ModelSerializer):
    # StartupDetails is a foreign key, linking NonFunctionalRequirements to StartupDetails
    startup = serializers.PrimaryKeyRelatedField(queryset=StartupDetails.objects.all(), required=True)

    class Meta:
        model = NonFunctionalRequirements
        fields = [
            'id', 
            'startup',  # This will hold the foreign key to StartupDetails
            'response_time', 
            'throughput', 
            'authentication', 
            'authorization', 
            'uptime', 
            'backup', 
            'recovery', 
            'monitoring', 
            'budget', 
            'cost_estimation', 
            'licensing'
        ]
