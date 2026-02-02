from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('languages/', views.languages_list, name='languages_list'),
    path('language/<int:id>/', views.language_detail, name='language_detail'),
    # -------- BRITISH QUIZ --------
    path('quiz/british/', views.british_quiz_start, name='british_quiz'),
    path('quiz/british/<int:index>/', views.british_quiz, name='british_quiz_question'),
    path('quiz/british/result/', views.british_quiz_result, name='british_quiz_result'),
    # SPANISH QUIZ
    path('quiz/spanish/', views.spanish_quiz_start, name='spanish_quiz'),
    path('quiz/spanish/<int:index>/', views.spanish_quiz, name='spanish_quiz_question'),
    path('quiz/spanish/result/', views.spanish_quiz_result, name='spanish_quiz_result'),
    #chineese quiz
    path('quiz/chinese/', views.chinese_quiz_start, name='chinese_quiz_start'),
    path('quiz/chinese/<int:index>/', views.chinese_quiz, name='chinese_quiz_question'),
    path('quiz/chinese/result/', views.chinese_quiz_result, name='chinese_quiz_result'),
    #Rusiian QUIZ
    path('quiz/russian/', views.russian_quiz_start, name='russian_quiz_start'),
    path('quiz/russian/<int:index>/', views.russian_quiz, name='russian_quiz_question'),
   path('quiz/russian/result/', views.russian_quiz_result, name='russian_quiz_result'),

]
