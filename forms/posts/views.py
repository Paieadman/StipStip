import json
from dataclasses import dataclass, asdict

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


@api_view(['GET','POST'])
def get_question(request):
    if request.method == 'POST':
        print()
    else:
        questions = Question.objects.filter(id=1).first()
        print(questions.question_text)
        for var in AnswerVariant.objects.filter(question_father_id=questions.id):
            print(var.description)
        data_variants = []
        for var in AnswerVariant.objects.filter(question_father_id=questions.id):
            data_variants.append(AnswerAnswer(var.id, var.description))
            print(var.description)
        # print( "description" + data_variants[0])

        ans_data = {
            "question": questions.question_text,
            "answers": data_variants,
        }
        print(ans_data)
        return JsonResponse(json.dumps(ans_data, ensure_ascii=False), safe=False)