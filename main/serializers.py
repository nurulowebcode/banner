from rest_framework import serializers
from .models import *


class BannerSer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class Service_Section_InfoSer(serializers.ModelSerializer):
    class Meta:
        model = Service_Section_Info
        fields = "__all__"


class ServiceSer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class About_UsSer(serializers.ModelSerializer):
    class Meta:
        model = About_Us
        fields = "__all__"


class About_Us_InfoSer(serializers.ModelSerializer):
    class Meta:
        model = About_Us_Info
        fields = "__all__"


class ContactSer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class InfoSer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class TestimonialSer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class Partner_BrandSer(serializers.ModelSerializer):
    class Meta:
        model = Partner_Brand
        fields = "__all__"







