from django.urls import path
from .views import GetArchitectureDiagram

urlpatterns = [
    path('getArchitecture', GetArchitectureDiagram.as_view(), name='getArchitecture')
]
