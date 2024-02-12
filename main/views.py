from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def get_banner(request):
    banner = Banner.objects.last()
    ser = BannerSer(banner)
    return Response(ser.data)


@api_view(['GET'])
def get_service_info(request):
    service_info = Service_Section_Info.objects.last()
    ser = Service_Section_InfoSer(service_info)
    return Response(ser.data)


@api_view(['GET'])
def get_service(request):
    service = Service.objects.all().order_by('-id')[:3]
    ser = ServiceSer(service, many=True)
    return Response(ser.data)


@api_view(['POST'])
def create_contact(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    Contact.objects.create(
        full_name=full_name,
        email=email,
        phone_number=phone_number,
    )
    return Response({"message": "created"})









