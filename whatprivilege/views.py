from django.shortcuts import render_to_response
from whatprivilege.models import Question
from whatprivilege.models import WorkshopQuestion
from whatprivilege.models import Workshop
from django.template import RequestContext
import uuid
from md5 import md5

def home(request):
    #logics .... 
    return render_to_response('home.html', {}) 

def instructions(request): 
    #logics....
    return render_to_response('instructions.html',{})

def makeWorkshop(request):
    if request.method == 'POST':
        url=str(md5(str(uuid.uuid4())).hexdigest())
        while (Workshop.objects.filter(urlCode=url).exists()) :
            url=str(md5(str(uuid.uuid4())).hexdigest())        
        new_wokshop = Workshop(urlCode=url)
        new_workshop.save()
        qs = Question.objects
        for q in qs :
            wq = WorkshopQuestion(
                workshopID: new_workshop.id,
                qID: q.id,
                numberYes: 0,
                numberNo: 0
            )
            wq.save()
        context = {
            'url':'http://whatprivilege.me/'+url
        }
        return render_to_response('workshop.html', context)
    else:
    	context = RequestContext(request, {})
        return render_to_response('workshop.html', context)

def question(request):
    q_id = 0
    current_q = False
    cookie_set = False
    if request.method == 'POST':
        alldata = request.POST
        answer = alldata.get("yesno")
        current_q = Question.objects.get(id=alldata.get("qnumber"))
        # check if they have answered this question already
        if not request.COOKIES.has_key(str(current_q.id)) :
            if answer == 'yes':
                current_q.numberYes += 1
	    elif answer == 'no':
	        current_q.numberNo += 1
	    current_q.save()
        else : # cookie was already set
            cookie_set = True
        q_id = current_q.id
    question = get_question(q_id)

    # most cases - load next question
    if question :
        context = {
             'question': question,
        } 
        context = RequestContext(request, context)
        response = render_to_response('question.html', context) 
        if not cookie_set and current_q :
            response.set_cookie(str(current_q.id), 'answered')
        return response

    # we have iterated through all questions
    else :
    	questions = Question.objects.order_by('pk')
    	context = {
    		'questions': questions,
    	}
    	response = render_to_response('results.html', context) 
        if not cookie_set and current_q:
            response.set_cookie(str(current_q.id), 'answered')
        return response

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

