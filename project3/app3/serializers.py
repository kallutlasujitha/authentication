from rest_framework import serializers
from .models import *



# class studentserializer(serializers.ModelSerializer):
#     class Meta:
#         fields='__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'
        