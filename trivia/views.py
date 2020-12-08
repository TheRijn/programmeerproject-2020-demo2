from django.shortcuts import render


def questions(request):
    questions = None

    return render(request, 'trivia/index.html', {
        'questions': questions
    })
