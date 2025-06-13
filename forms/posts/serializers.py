from django.contrib.auth import authenticate
from rest_framework import serializers


from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'login', 'password', 'token', 'lastname', 'middlename', 'firstname' ]

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    # email = serializers.CharField(max_length=255)
    login = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        print(data)
        login = data.get('login', None)
        password = data.get('password', None)

        if login is None:
            raise serializers.ValidationError(
                'An login is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=login, password=password)

        # Если пользователь с данными почтой/паролем не найден, то authenticate
        # вернет None. Возбудить исключение в таком случае.
        if user is None:
            raise serializers.ValidationError(
                'A user with this login and password was not found.'
            )

        # Django предоставляет флаг is_active для модели User. Его цель
        # сообщить, был ли пользователь деактивирован или заблокирован.
        # Проверить стоит, вызвать исключение в случае True.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # Метод validate должен возвращать словать проверенных данных. Это
        # данные, которые передются в т.ч. в методы create и update.
        return {
            'email': user.email,
            'login': user.login,
            'token': user.token
        }

# class ProfileSerializer(serializers.ModelSerializer):
#
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['email', 'login', 'lastname' ]
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)