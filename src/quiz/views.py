from django.shortcuts import render
from .forms import QuizForm
from .models import Quize
from .formula import *









def homepage(request):
    pass


def quiz(request):

    if request.method == 'POST':
        print("----------REQUEST.POST------------")
        print(request.POST)
        print(request.session.session_key)

        sports = formula(request.POST.dict())




        quiz_form = QuizForm(data=request.POST)
        #print("----------QUIZFORM------------")
        #print(quiz_form)
        if quiz_form.is_valid():
            quiz_form.save()

        return render(request,
                        'quiz/post/result.html',
                        {
                        'sports':sports,
                        })

    quiz_form = QuizForm()
    return render(request,
                    'quiz/post/form.html',
                    {
                    'quiz_form':quiz_form,
                    })



# Create your views here.
