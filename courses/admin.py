from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.utils.html import format_html
from .models import Language, Course, Lesson, BasicExercise, Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'photo_preview')
    fields = ('name', 'bio', 'rating', 'photo')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:50%;">',
                obj.photo.url
            )
        return "No Image"

    photo_preview.short_description = "Photo"


# Only register the models you want to show
admin.site.register(Language)
admin.site.register(Teacher, TeacherAdmin)


# ----------------------------
# Unregister models (if they were registered elsewhere)
# ----------------------------
try:
    admin.site.unregister(Course)
except NotRegistered:
    pass

try:
    admin.site.unregister(Lesson)
except NotRegistered:
    pass

try:
    admin.site.unregister(BasicExercise)
except NotRegistered:
    pass
