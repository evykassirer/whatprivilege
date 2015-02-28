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
        new_workshop = Workshop(urlCode=url)
        new_workshop.save()
        qs = Question.objects.all()
        for q in qs :
            wq = WorkshopQuestion(
                workshopID= new_workshop.id,
                qID= q.id,
                numberYes= 0,
                numberNo= 0
            )
            wq.save()
        context = {
            'url':'http://whatprivilege.me/workshop-code/'+url
        }
        return render_to_response('workshop.html', context)
    else:
    	context = RequestContext(request, {})
        return render_to_response('workshop.html', context)

def loadWorkshop(request, code):
	response = render_to_response('home.html')
	try:
	    w = Workshop.objects.get(urlCode=code)
	except Workshop.DoesNotExist:
	    return response
	response.set_cookie('workshop', str(w.id))
	return response	

def question(request):
    q_id = None
    current_q = False
    cookie_set = False
    workshop = None

    if request.COOKIES.has_key("workshop") :
        workshop = request.COOKIES["workshop"] or None
    
    if request.method != 'POST':
        question_number = 0
        context = {
             'question_number': question_number,
        }
        context = RequestContext(request, context)
        response = render_to_response('question.html', context) 
        return response        
    
    alldata = request.POST
    if alldata.get("qnumber") != "": 
        answer = alldata.get("yesno")
        current_q = Question.objects.get(id=alldata.get("qnumber"))
        # check if they have not answered this question already
        if not request.COOKIES.has_key(str(current_q.id)) and current_q != 0 :
            w = False
            if workshop is not None:
                w = WorkshopQuestion.objects.filter(workshopID=workshop, qID=current_q.id).first()
            if answer == 'yes':
                current_q.numberYes += 1
                if w:
                    w.numberYes += 1
    	    elif answer == 'no':
    	        current_q.numberNo += 1
                if w:
                    w.numberNo += 1
    	    current_q.save()
            if w:
                w.save()         
        else : # cookie was already set, or we just posted from the empty form
            cookie_set = True
        q_id = current_q.id
    question = get_question(q_id)

    # most cases - load next question
    if question :
        question_number = get_question_number(question.id) or 1
        question_total = get_question_total() or 1
        context = {
             'question': question,
             'percent_no': get_percent_no(question.numberYes, question.numberNo),
             'question_number': question_number,
             'question_total': question_total,
        }
        if workshop is not None:
            w = WorkshopQuestion.objects.filter(workshopID=workshop, qID=question.id).first()
            context['workshop_percent_no'] = get_percent_no(w.numberYes, w.numberNo)
        context = RequestContext(request, context)
        response = render_to_response('question.html', context) 
        if not cookie_set and current_q :
            response.set_cookie(str(current_q.id), 'answered')
        return response

    # we have iterated through all questions
    else :
    	questions = Question.objects.order_by('pk')

        for question in questions:
            question.percent = get_percent_no(question.numberYes, question.numberNo)

    	context = {
    		'questions': questions,
    	}
    	response = render_to_response('results.html', context) 
        if not cookie_set and current_q:
            response.set_cookie(str(current_q.id), 'answered')
        return response

def error404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
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

def get_percent_no(yes, no):
    if yes + no == 0:
        return 0
    return int(round(
        float(no) / float(yes + no),
        2
    ) * 100)

def get_question_total():
    return Question.objects.all().count()

def get_question_number(id):
    return Question.objects.filter(id__lt=id).count() + 1
