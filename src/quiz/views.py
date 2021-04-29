from django.shortcuts import render
from .forms import QuizForm







def homepage(request):
    pass


def quiz(request):
    quiz_form = QuizForm()
    return render(request,
                    'quiz/post/form.html',
                    {
                    'quiz_form':quiz_form,
                    }

                        )



# Create your views here.
