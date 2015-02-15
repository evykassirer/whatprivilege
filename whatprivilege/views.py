from django.shortcuts import render_to_response
#from whatprivilege.models import Question

def home(request):
    #logics .... 
    return render_to_response('home.html', {}) 

def instructions(request): 
    #logics....
    return render_to_response('instructions.html',{})

def question(request, question_id):
    #logics...
    return render_to_response('question.html', {"question":"test"}) 

def learned(request):
    #logics...
    return render_to_response('learned.html', {})

