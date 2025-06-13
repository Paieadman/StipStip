import datetime

import jwt
from django.db import models
from django.db.models import ForeignKey
from django.conf import settings
from django.contrib.auth.models import (
AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from datetime import datetime, timedelta


class Question(models.Model):
    question_text = models.CharField()

class AnswerVariant(models.Model):
    description = models.CharField()
    question_father = ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True, related_name='which_question')
    next_question = ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True, related_name='next_question')

class UserManager(BaseUserManager):
    def create_user(self, login, email, firstname, lastname, middlename, password=None, ):
        if login is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            login=login,
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            middlename=middlename,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, login, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(login, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True,)
    lastname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    # role = models.CharField(max_length=255, default="Student")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Дополнительный поля, необходимые Django
    # при указании кастомной модели пользователя.

    # Свойство USERNAME_FIELD сообщает нам, какое поле мы будем использовать
    # для входа в систему. В данном случае мы хотим использовать почту.
    USERNAME_FIELD = 'login'
    # REQUIRED_FIELDS = ['login']

    # Сообщает Django, что определенный выше класс UserManager
    # должен управлять объектами этого типа.
    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.login

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.login

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.login

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        print("payload = " + str(payload['id']))

        return token


