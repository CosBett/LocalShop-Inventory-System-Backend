from rest_framework import serializers
from .models import Admin, Clerk, User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }
     

class AdminSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'password2', 'is_admin']

        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance       
   
    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})
        user.set_password(password)
        user.is_admin = True
        user.save()
        Admin.objects.create(user=user)
        return user


class ClerkSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'is_staff']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})
        user.set_password(password)
        user.is_staff = True

        user.save()
        Clerk.objects.create(user=user)
        return user
