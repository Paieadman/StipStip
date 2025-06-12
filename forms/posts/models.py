from django.db import models

# Create your models here.
from django.db import models
from django.db.models import ForeignKey


class Question(models.Model):
    question_text = models.CharField()

class AnswerVariant(models.Model):
    description = models.CharField()
    # question_father = ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='which_question')
    question_father = ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True, related_name='which_question')
    # next_question_id = ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='next_question')
    next_question = ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True, related_name='next_question')

