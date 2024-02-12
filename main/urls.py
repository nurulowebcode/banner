from django.urls import path
from .views import *

urlpatterns = [
    path('get-banner/', get_banner),
    path('get-service-info/', get_service_info),
    path('get-all-services/', get_service),
    path('create-contact-api/', create_contact),
]