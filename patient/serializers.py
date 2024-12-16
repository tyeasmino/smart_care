from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)

    class Meta:
        model = models.Patient
        fields = '__all__' 



class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']    
        email = self.validated_data['email']    
        first_name = self.validated_data['first_name']    
        last_name = self.validated_data['last_name']    
        password = self.validated_data['password']    
        confirm_password = self.validated_data['confirm_password']     

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email already exists"})

        if password != confirm_password:
            raise serializers.ValidationError({'error' : "Password doesn't Matched"})
        
        account = User(username=username, email=email, first_name=first_name, last_name=last_name)
        account.set_password(password) 
        account.is_active = False
        account.save()
        return account

    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    