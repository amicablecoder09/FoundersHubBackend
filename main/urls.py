from django.contrib import admin
from django.urls import path
from .views import TestAPIView, CreateStartupWithRequirementsAPIView, RetrieveStartupWithRequirementsAPIView, ListStartupsWithRequirementsAPIView

urlpatterns = [
    path('', TestAPIView.as_view(), name='test api view'),
    path('CreateStartup', CreateStartupWithRequirementsAPIView.as_view(), name='create startup'),
    path('startups/<int:startup_id>/', RetrieveStartupWithRequirementsAPIView.as_view(), name='retrieve_startup_with_requirements'),
    path('startups/list/', ListStartupsWithRequirementsAPIView.as_view(), name='list_startups_with_requirements'),
]