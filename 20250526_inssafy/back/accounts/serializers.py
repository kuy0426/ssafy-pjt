from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        return data
    
    def save(self, request):
        user = super().save(request)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'date_joined', 'biography', 'profile_image')

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('biography', 'profile_image')
        extra_kwargs = {
            'biography': {'required': False},
            'profile_image': {'required': False},
        }