from django.shortcuts import render_to_response
from whatprivilege.models import Question

def home(request):
    #logics .... 
    return render_to_response('home.html', {}) 

def instructions(request): 
    #logics....
    return render_to_response('instructions.html',{})

def question(request):
    question = get_question()

    context = {
        'question': question,
    }
    return render_to_response('question.html', context) 

def learned(request):
    #logics...
    return render_to_response('learned.html', {})

#-------------------- Helper Functions

def get_question(previous=None):
    question = None
    if not previous:
        question = Question.objects.order_by('pk').first()
    else:
        question = Question.objects.filter(id__gt=previous).first()
    return question

