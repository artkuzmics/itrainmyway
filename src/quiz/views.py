from django.shortcuts import render
from .forms import QuizForm, EnquiryForm
from .models import Quize
from .formula import *
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, reverse




def thankyou(request):
    return render(request,'quiz/post/thankyou.html',)


def homepage(request):
    return render(request,'quiz/homepage.html',)


def partners(request):


    if request.method == 'POST':

        enquiry_form = EnquiryForm(data = request.POST)

        if enquiry_form.is_valid():
            new_enquiry = enquiry_form.save(commit=False)
            new_enquiry.save()

            return render(request, 'quiz/post/thankyou.html')

    enquiry_form = EnquiryForm()

    return render(request,'quiz/partners.html', {'enquiry_form':enquiry_form})


def results(request):

    sports = ['Ice Skating', 'Latin Dancing', 'Pole fitness', 'Canoeing', 'Running', 'Cycling', 'Rock Climbing', 'Acro Yoga', 'Trampolining']

    if request.method == 'POST':

            print("----------REQUEST.POST------------")
            print(request.POST)
            print(request.session.session_key)

            chosen_sports = list(dict(request.POST).keys())[1:-1]

            print(chosen_sports)

            return redirect(reverse('quiz:results'))

    return render(request,'quiz/post/result.html',{'sports':sports,})


def quiz(request):

    if request.method == 'POST':
        if "likely to recommend" in request.POST:

            quiz_entry = get_object_or_404(Quize, session_key=request.session.session_key)

            chosen_sports = list(dict(request.POST).keys())[1:-1]

            selected = ""
            for i, sport in enumerate(chosen_sports):
                selected += sport
                if i < len(chosen_sports)-1:
                    selected += ", "

            quiz_entry.selected = selected
            quiz_entry.likely_to_recommend = request.POST["likely to recommend"]

            quiz_entry.save()

            request.session.flush()

            return render(request, 'quiz/post/thankyou.html')

            #redirect(reverse('quiz:homepage'))



        else:


            if not request.session or not request.session.session_key:
                request.session.save()


            sports = formula(request.POST.dict())

            quiz_form = QuizForm(data=request.POST)
            if quiz_form.is_valid():
                new_entry = quiz_form.save(commit=False)
                new_entry.session_key = request.session.session_key

                new_entry.save()

                print(sports)

                return render(request,'quiz/post/result.html',{'sports':sports,})


    quiz_form = QuizForm()
    return render(request,
                    'quiz/post/form.html',
                    {
                    'quiz_form':quiz_form,
                    })



# Create your views here.
