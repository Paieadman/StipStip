import json
from dataclasses import dataclass, asdict

from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

# Create your views here.
from .forms import CreateQuestion
from .models import Question, AnswerVariant


# from .models import genData


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

# @dataclass()
class AnswerAnswer(dict):
    # answer_id: int
    # question_text: str
    def __init__(self, answer_id, question_text):
        dict.__init__(self, answer_id = answer_id, question_text = question_text)
        # self.answer_id = answer_id
        # self.question_text = question_text

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    # def toJSON(self):
    #     return json.dumps(
    #         self,
    #         default=lambda o: o.__dict__,
    #         sort_keys=True,
    #         indent=4)

class UserVoteModel:
    def __init__(self, user_id, variant_id, question_id):
        self.user_id = user_id
        self.variant_id = variant_id
        self.question_id = question_id


class UserVoteModelSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    variant_id = serializers.IntegerField()
    question_id = serializers.IntegerField()


@api_view(['GET','POST'])
def get_question(request):
    if request.method == 'POST':
        print(request.data)
        serializer = UserVoteModelSerializer(data=request.data)
        if serializer.is_valid():
            return save_user_answer(
                serializer.validated_data['user_id'],
                serializer.validated_data['variant_id'],
                serializer.validated_data['question_id'],
            )


            # return HttpResponse("OK1 validated")
        else:
            return HttpResponse("NOK")
    else:
        return get_and_send_next()

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