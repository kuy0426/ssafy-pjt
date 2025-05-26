from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        return data
    
    def save(self, request):
        user = super().save(request)
        user.save()
        return user
