from django.db import models
from courses.models import Lesson


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
