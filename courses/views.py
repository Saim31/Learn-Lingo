from django.shortcuts import render, redirect
from .models import Language, Course, Teacher
from django.contrib.auth.decorators import login_required
from django.shortcuts import render




# ---------------- HOME ----------------
@login_required
def home(request):
    languages = Language.objects.all()
    return render(request, 'home.html', {'languages': languages})


# ---------------- LANGUAGE LIST ----------------
def languages_list(request):
    languages = Language.objects.all()
    return render(request, 'courses/languages.html', {'languages': languages})


# ---------------- LANGUAGE DETAIL ----------------
def language_detail(request, id):
    language = Language.objects.get(id=id)
    courses = Course.objects.filter(language=language)
    teachers = Teacher.objects.all()

    for teacher in teachers:
        teacher.rating_percent = teacher.rating * 20

    return render(request, 'courses/language_detail.html', {
        'language': language,
        'courses': courses,
        'teachers': teachers
    })


# =================================================
# ============ BRITISH QUIZ (FILE BASED) ===========
# =================================================
from django.shortcuts import render, redirect
from .quiz_data.british import BRITISH_QUIZ


def british_quiz_start(request):
    request.session['british_score'] = 0
    request.session['wrong_answers'] = []
    return redirect('british_quiz_question', index=0)


def british_quiz(request, index):
    total = len(BRITISH_QUIZ)

  
    if 'british_score' not in request.session:
        request.session['british_score'] = 0

    if 'wrong_answers' not in request.session:
        request.session['wrong_answers'] = []

    if index >= total:
        return redirect('british_quiz_result')

    question = BRITISH_QUIZ[index]

    if request.method == 'POST':
        selected = request.POST.get('answer')

        if selected:
            if selected.lower() == question['correct'].lower():
                request.session['british_score'] += 1
            else:
                wrong = {
                    "question": question["question"],
                    "selected": selected,
                    "correct": question["correct"]
                }
                request.session['wrong_answers'].append(wrong)

        return redirect('british_quiz_question', index=index + 1)

    return render(request, 'courses/quiz_question.html', {
        'question': question,
        'index': index + 1,
        'total': total
    })


def british_quiz_result(request):
    score = request.session.get('british_score', 0)
    total = len(BRITISH_QUIZ)
    percentage = round((score / total) * 100, 2)
    wrong_answers = request.session.get('wrong_answers', [])

    # Reset after showing result
    request.session['british_score'] = 0
    request.session['wrong_answers'] = []

    return render(request, 'courses/quiz_result.html', {
        'score': score,
        'total': total,
        'percentage': percentage,
        'wrong_answers': wrong_answers
    })

from django.shortcuts import render, redirect
from .quiz_data.spanish import SPANISH_QUIZ


def spanish_quiz_start(request):
    request.session['spanish_score'] = 0
    request.session['spanish_wrong_answers'] = []
    return redirect('spanish_quiz_question', index=0)


def spanish_quiz(request, index):
    total = len(SPANISH_QUIZ)

    if index >= total:
        return redirect('spanish_quiz_result')

    question = SPANISH_QUIZ[index]

    if request.method == 'POST':
        selected = request.POST.get('answer')

        # score count
        if selected == question['correct']:
            request.session['spanish_score'] += 1
        else:
            wrong = request.session.get('spanish_wrong_answers', [])
            wrong.append({
                "question": question['question'],
                "selected": selected,
                "correct": question['correct']
            })
            request.session['spanish_wrong_answers'] = wrong

        return redirect('spanish_quiz_question', index=index + 1)

    return render(request, 'courses/quiz_question.html', {
        'question': question,
        'index': index + 1,
        'total': total
    })


def spanish_quiz_result(request):
    score = request.session.get('spanish_score', 0)
    total = len(SPANISH_QUIZ)

    # calculate percentage
    percentage = 0
    if total > 0:
        percentage = round((score / total) * 100, 2)

    wrong_answers = request.session.get('spanish_wrong_answers', [])

    return render(request, 'courses/quiz_result.html', {
        'score': score,
        'total': total,
        'percentage': percentage,
        'wrong_answers': wrong_answers,
        'language_name': 'Spanish'
    })

from django.shortcuts import render, redirect
from .quiz_data.chinese import CHINESE_QUIZ


def chinese_quiz_start(request):
    request.session['chinese_score'] = 0
    request.session['chinese_wrong_answers'] = []
    return redirect('chinese_quiz_question', index=0)


def chinese_quiz(request, index):
    total = len(CHINESE_QUIZ)

    if index >= total:
        return redirect('chinese_quiz_result')

    question = CHINESE_QUIZ[index]

    if request.method == 'POST':
        selected = request.POST.get('answer')

        if selected == question['correct']:
            request.session['chinese_score'] += 1
        else:
            wrong = request.session.get('chinese_wrong_answers', [])
            wrong.append({
                "question": question['question'],
                "selected": selected,
                "correct": question['correct']
            })
            request.session['chinese_wrong_answers'] = wrong

        return redirect('chinese_quiz_question', index=index + 1)

    return render(request, 'courses/quiz_question.html', {
        'question': question,
        'index': index + 1,
        'total': total
    })


def chinese_quiz_result(request):
    score = request.session.get('chinese_score', 0)
    total = len(CHINESE_QUIZ)

    percentage = 0
    if total > 0:
        percentage = round((score / total) * 100, 2)

    wrong_answers = request.session.get('chinese_wrong_answers', [])

    return render(request, 'courses/quiz_result.html', {
        'score': score,
        'total': total,
        'percentage': percentage,
        'wrong_answers': wrong_answers,
        'language_name': 'Chinese'
    })


from .quiz_data.russian import RUSSIAN_QUIZ


def russian_quiz_start(request):
    request.session['russian_score'] = 0
    request.session['russian_wrong_answers'] = []
    return redirect('russian_quiz_question', index=0)


def russian_quiz(request, index):
    total = len(RUSSIAN_QUIZ)

    if index >= total:
        return redirect('russian_quiz_result')

    question = RUSSIAN_QUIZ[index]

    if request.method == 'POST':
        selected = request.POST.get('answer')

        # score count
        if selected == question['correct']:
            request.session['russian_score'] += 1
        else:
            wrong = request.session.get('russian_wrong_answers', [])
            wrong.append({
                "question": question['question'],
                "selected": selected,
                "correct": question['correct']
            })
            request.session['russian_wrong_answers'] = wrong

        return redirect('russian_quiz_question', index=index + 1)

    return render(request, 'courses/quiz_question.html', {
        'question': question,
        'index': index + 1,
        'total': total
    })


def russian_quiz_result(request):
    score = request.session.get('russian_score', 0)
    total = len(RUSSIAN_QUIZ)

    percentage = 0
    if total > 0:
        percentage = round((score / total) * 100, 2)

    wrong_answers = request.session.get('russian_wrong_answers', [])

    return render(request, 'courses/quiz_result.html', {
        'score': score,
        'total': total,
        'percentage': percentage,
        'wrong_answers': wrong_answers,
        'language_name': 'Russian'
    })
