from django.contrib import admin
from .models import (
    StartupDetails, NonFunctionalRequirements, FunctionalRequirements, Scalability,
    Deployment, Performance, Security, Reliability, Maintainability, Cost
)


@admin.register(StartupDetails)
class StartupDetailsAdmin(admin.ModelAdmin):
    list_display = ('startup_name', 'business_domain', 'product_type')
    search_fields = ('startup_name', 'business_domain', 'product_type')
    list_filter = ('business_domain', 'product_type')


@admin.register(NonFunctionalRequirements)
class NonFunctionalRequirementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'startup')
    search_fields = ('startup__startup_name',)
    list_filter = ('startup__startup_name',)


@admin.register(FunctionalRequirements)
class FunctionalRequirementsAdmin(admin.ModelAdmin):
    list_display = ('startup', 'business_domain')
    search_fields = ('startup__startup_name', 'business_domain')
    list_filter = ('startup__startup_name', 'business_domain')


@admin.register(Scalability)
class ScalabilityAdmin(admin.ModelAdmin):
    list_display = ('startup', 'expected_number_of_users', 'expected_number_of_transactions_per_second')
    search_fields = ('startup__startup_name',)
    list_filter = ('startup__startup_name', 'expected_number_of_users')


@admin.register(Deployment)
class DeploymentAdmin(admin.ModelAdmin):
    list_display = ('startup', 'cloud_provider', 'deployment_model')
    search_fields = ('startup__startup_name', 'cloud_provider', 'deployment_model')
    list_filter = ('startup__startup_name', 'cloud_provider', 'deployment_model')


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('startup', 'response_time', 'throughput')
    search_fields = ('startup__startup_name', 'response_time', 'throughput')
    list_filter = ('startup__startup_name',)


@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    list_display = ('startup', 'authentication', 'authorization')
    search_fields = ('startup__startup_name', 'authentication', 'authorization')
    list_filter = ('startup__startup_name',)


@admin.register(Reliability)
class ReliabilityAdmin(admin.ModelAdmin):
    list_display = ('startup', 'uptime', 'backup', 'recovery')
    search_fields = ('startup__startup_name', 'uptime', 'backup', 'recovery')
    list_filter = ('startup__startup_name',)


@admin.register(Maintainability)
class MaintainabilityAdmin(admin.ModelAdmin):
    list_display = ('startup', 'code_quality', 'documentation', 'monitoring')
    search_fields = ('startup__startup_name', 'code_quality', 'documentation', 'monitoring')
    list_filter = ('startup__startup_name',)


@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ('startup', 'budget', 'cost_estimation', 'licensing')
    search_fields = ('startup__startup_name', 'budget', 'cost_estimation', 'licensing')
    list_filter = ('startup__startup_name',)
