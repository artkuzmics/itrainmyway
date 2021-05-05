from django.shortcuts import render
from .forms import QuizForm, EnquiryForm
from .models import Quize
from .formula import *
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, reverse
import json




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

    sports = ['Ice_Skating', 'Latin_Dancing', 'Pole_fitness', 'Canoeing', 'Running', 'Cycling', 'Rock_Climbing', 'Acro_Yoga', 'Trampolining']

    if request.method == 'POST':

            print("----------REQUEST.POST------------")
            print(request.POST)
            print(request.session.session_key)

            chosen_sports = list(dict(request.POST).values())[1:-1]

            yes = ""
            no = ""

            for sport in chosen_sports:
                json_acceptable = sport[0].replace("'","\"")
                s = json.loads(json_acceptable)

                if list(s.keys())[0] == "yes":
                    yes += s["yes"]
                    yes += ", "
                else:
                    no += s["no"]
                    no += ", "


            print('yes',yes)
            print('no',no)

            return render(request, 'quiz/post/thankyou.html')


    return render(request,'quiz/post/results.html',{'sports':sports,})


def quiz(request):

    if request.method == 'POST':
        if "likely to recommend" in request.POST:

            quiz_entry = get_object_or_404(Quize, session_key=request.session.session_key)

            chosen_sports = list(dict(request.POST).values())[1:-1]

            yes = ""
            no = ""

            for sport in chosen_sports:
                json_acceptable = sport[0].replace("'","\"")
                s = json.loads(json_acceptable)

                if list(s.keys())[0] == "yes":
                    yes += s["yes"]
                    yes += ", "
                else:
                    no += s["no"]
                    no += ", "

            quiz_entry.yes = yes
            quiz_entry.no = no            
            quiz_entry.likely_to_recommend = request.POST["likely to recommend"]

            quiz_entry.save()

            request.session.flush()

            return render(request, 'quiz/post/thankyou.html')

            #redirect(reverse('quiz:homepage'))



        else:


            if not request.session or not request.session.session_key:
                request.session.save()


            sports = formula(request.POST.dict())

            print(sports)

            quiz_form = QuizForm(data=request.POST)
            if quiz_form.is_valid():
                new_entry = quiz_form.save(commit=False)
                new_entry.session_key = request.session.session_key

                new_entry.save()

                print(sports)

                return render(request,'quiz/post/results.html',{'sports':sports,})


    quiz_form = QuizForm()
    return render(request,
                    'quiz/post/form.html',
                    {
                    'quiz_form':quiz_form,
                    })



# Create your views here.
