import json
from dataclasses import dataclass, asdict

from django.contrib.auth import logout, login
from rest_framework import serializers, status
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .forms import CreateQuestion
from .models import Question, AnswerVariant
from .renderers import UserJSONRenderer
from .serializers import RegistrationSerializer, LoginSerializer


def post_new(request):
    if request == 'POST':
        form = CreateQuestion(request.POST, request.FILES)
        if form.is_valid():
            print("")
            # save with user
        return redirect('posts:list')
    else:
        form = CreateQuestion()
    return render(request, 'posts/question.html', { 'form' : form})


def post_list(request):
    return render(request, 'posts/post_list.html')

class GetQuestionResponse:
    def __init__(self, que, data):
        self.que = que,
        self.data = data,

class AnswerAnswer(dict):
    def __init__(self, answer_id, question_text):
        dict.__init__(self, answer_id = answer_id, question_text = question_text)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class UserVoteModel:
    def __init__(self, user_id, variant_id, question_id):
        self.user_id = user_id
        self.variant_id = variant_id
        self.question_id = question_id


class UserVoteModelSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    variant_id = serializers.IntegerField()
    question_id = serializers.IntegerField()




# @api_view(['GET','POST'])
# def get_question(request):
#     # if request.user is not None and request.user.isauthenticated():
#     #     print("yes")
#     # else:
#     #     print("No")
#     # print(request.user)
#
#     if request.method == 'POST':
#         print(request.data)
#         serializer = UserVoteModelSerializer(data=request.data)
#         if serializer.is_valid():
#             return save_user_answer(
#                 serializer.validated_data['user_id'],
#                 serializer.validated_data['variant_id'],
#                 serializer.validated_data['question_id'],
#             )
#
#
#             # return HttpResponse("OK1 validated")
#         else:
#             return HttpResponse("NOK")
#     else:
#         return get_and_send_next()

def save_user_answer(user_id, variant_id, question_id=1):
    print("TODO save")
    ans = AnswerVariant.objects.get(id=variant_id)
    return get_and_send_next(question_id=ans.next_question_id)

def get_and_send_next(question_id=1):
    if question_id is  None:
        return HttpResponse("Done")
    questions = Question.objects.get(id=question_id)
    for var in AnswerVariant.objects.filter(question_father_id=questions.id):
        print(var.description)
    data_variants = []
    for var in AnswerVariant.objects.filter(question_father_id=questions.id):
        data_variants.append(AnswerAnswer(var.id, var.description))
        print(var.description)

    ans_data = {
        "question": questions.question_text,
        "answers": data_variants,
    }
    print(ans_data)
    return JsonResponse(ans_data, safe=False)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        print(request.data)
        # user = request.data.get('user', {})

        # Обратите внимание, что мы не вызываем метод save() сериализатора, как
        # делали это для регистрации. Дело в том, что в данном случае нам
        # нечего сохранять. Вместо этого, метод validate() делает все нужное.
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)

        # return Response({serializer.data['login'], serializer.data['token']}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        # user = request.data.get('user', {})
        user = request.data
        print(request.data)
        # login = request.data.get()

        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET','POST'])
# def get_question(request):
#     # if request.user is not None and request.user.isauthenticated():
#     #     print("yes")
#     # else:
#     #     print("No")
#     # print(request.user)
#
#     if request.method == 'POST':
#         print(request.data)
#         serializer = UserVoteModelSerializer(data=request.data)
#         if serializer.is_valid():
#             return save_user_answer(
#                 serializer.validated_data['user_id'],
#                 serializer.validated_data['variant_id'],
#                 serializer.validated_data['question_id'],
#             )
#
#
#             # return HttpResponse("OK1 validated")
#         else:
#             return HttpResponse("NOK")
#     else:
#         return get_and_send_next()

class GetQuestionAPIView(APIView):
    # authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    # serializer_class = LoginSerializer

    def post(self, request):
        print(request.data)
        serializer = UserVoteModelSerializer(data=request.data)
        if serializer.is_valid():
            return save_user_answer(
                serializer.validated_data['user_id'],
                serializer.validated_data['variant_id'],
                serializer.validated_data['question_id'],
            )
        else:
            return HttpResponseBadRequest

    def get(self, request):
        return get_and_send_next()
        # print(request.data)
        # user = request.data.get('user', {})
        #
        # # Обратите внимание, что мы не вызываем метод save() сериализатора, как
        # # делали это для регистрации. Дело в том, что в данном случае нам
        # # нечего сохранять. Вместо этого, метод validate() делает все нужное.
        # serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        #
        # # return Response({serializer.data['login'], serializer.data['token']}, status=status.HTTP_200_OK)
        # return Response(serializer.data, status=status.HTTP_200_OK)

class GetQuestionAPIView(APIView):
    # authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    # serializer_class = LoginSerializer

    def post(self, request):
        print(request.data)
        print(request.user)
        serializer = UserVoteModelSerializer(data=request.data)
        if serializer.is_valid():
            return save_user_answer(
                serializer.validated_data['user_id'],
                serializer.validated_data['variant_id'],
                serializer.validated_data['question_id'],
            )
        else:
            return HttpResponseBadRequest

    def get(self, request):
        return get_and_send_next()

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print("logout")
        logout(request)
        # request.user.is_active = False
        # request.user.save()
        return HttpResponse(status.HTTP_204_NO_CONTENT)

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        response = {
            "login" : user.login,
            "lastname" : user.lastname,
            "middlename" : user.middlename,
            "firstname" : user.firstname,
            "requests" : []

        }
        # request.user.is_active = False
        # request.user.save()
        return JsonResponse(response)
