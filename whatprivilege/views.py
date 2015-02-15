from django.shortcuts import render_to_response
from whatprivilege.models import Question
from django.template import RequestContext
from django.core.context_processors import csrf 

def home(request):
    #logics .... 
    return render_to_response('home.html', {}) 

def instructions(request): 
    #logics....
    return render_to_response('instructions.html',{})

def question(request):
    q_id = 1
    if request.method == 'POST':
        alldata = request.POST
        answer = alldata.get("yesno")
        current_q = Question.objects.get(id=alldata.get("qnumber"))
        if answer == 'yes':
        	current_q.numberYes += 1
        elif answer == 'no':
        	current_q.numberNo += 1
        current_q.save()
        q_id = current_q.id + 1
    question = get_question()
    context = {
        'question': question,
    } 
    context.update(csrf(request))   
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

