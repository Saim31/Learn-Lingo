
# Register your models here.
from django.contrib import admin
from .models import Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 3  # show 3 blank options by default

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'lesson')
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)
