from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'url', 'id', 'username', 'email',
            'is_active', 'is_staff'
        )
        read_only_fields = ('is_active', 'is_staff')
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


class RegistrationSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password 1'}
    )

    password2 = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password 2'}
    )

    token = serializers.CharField(max_length=256, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'token')

    def create(self, validated_data):
        if validated_data['password1'] != validated_data['password2']:
            raise serializers.ValidationError(
                'A passwords must match'
            )
        return User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            password=validated_data['password1'],
        )


class LoginSerialiser(serializers.Serializer):
    username = serializers.CharField(max_length=128, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    email = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'An username address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'token': user.token,
        }
