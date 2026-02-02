from django.db import models
from django.contrib.auth.models import User
from courses.models import Lesson   # adjust app name if different


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"
