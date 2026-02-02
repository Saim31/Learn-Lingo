from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(upload_to='language_icons/', blank=True, null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    rating = models.FloatField(default=4.5)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class BasicExercise(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='exercises')
    question_word = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question_word} ({self.language.name})"
