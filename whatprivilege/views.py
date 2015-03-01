"""All request-handling logic for whatprivilege app."""
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from whatprivilege.models import Question, Answer, Workshop
from whatprivilege.helpers import (
    get_next_question, get_question_number,
    get_question_total, get_percent_no)


def home(request):
    """
    Main landing page.
    """
    return render_to_response('home.html')


def instructions(request):
    """
    Renders instructions page to brief the user before they start answering
    questions.
    """
    return render_to_response('instructions.html')


def makeWorkshop(request):
    """
    Creates a new workshop (which lets us render a custom link URL).
    """
    context = {}
    if request.method == 'POST':
        new_workshop = Workshop()
        new_workshop.save()
        new_workshop.setup()
        context = {
            'code': new_workshop.code,
        }
    return render_to_response(
        'workshop.html',
        RequestContext(request, context))


def loadWorkshop(request, code):
    """
    Sets the user's cookie to a workshop being accessed (after they click on
    the custom link).
    """
    response = render_to_response('home.html')
    try:
        w = Workshop.objects.get(code=code)
    except Workshop.DoesNotExist:
        raise Http404('This workshop does not exist.')
    response.set_cookie('workshop', str(w.code))
    return response


def question(request):
    """
    Main survey logic. Renders a question that the user should answer, based on
    the state of the user's cookie and the user's workshop (if any).
    """
    current_q = None
    workshop = None
    already_answered = False

    # Get the workshop from the user's cookie (if there is one).
    workshop = None
    if "workshop" in request.COOKIES:
        workshop = Workshop.objects.get(
            code=request.COOKIES["workshop"]
        )

    if request.method == 'POST':
        # The user has submitted an answer to a question.
        is_yes = request.POST.get("yesno") == 'yes'
        current_q = Question.objects.get(
                id=request.POST.get("qnumber"))
        already_answered = str(current_q.id) in request.COOKIES
        if not already_answered:
            # The user has not answered this question yet. Count the response.
            answer = Answer(yes=is_yes, question=current_q, workshop=workshop)
            answer.save()

    question = get_next_question(
            current_q.id if current_q else 0, workshop=workshop)

    if question:
        # Display the new question to the user.
        question_number = get_question_number(question.id, workshop=workshop)
        question_total = get_question_total(workshop=workshop)
        context = {
             'question': question,
             'percent_no': get_percent_no(question),
             'question_number': question_number,
             'question_total': question_total,
        }
        if workshop:
            context['workshop_percent_no'] = get_percent_no(question, workshop)

        response = render_to_response(
                'question.html',
                RequestContext(request, context))
        if not already_answered and current_q:
            response.set_cookie(str(current_q.id), 'answered')
        return response

    else:
        # We have iterated through all questions. Display the results page.
        if workshop:
            questions = workshop.questions.all()
        else:
            questions = Question.objects.filter(workshop_only=False)

        for question in questions:
            question.percent = get_percent_no(question, workshop)

        context = {
            'questions': questions,
        }
        response = render_to_response('results.html', context)
        if not already_answered and current_q:
            response.set_cookie(str(current_q.id), 'answered')
        return response


def error404(request):
    """
    Render our custom 404 page.
    """
    response = render_to_response(
        '404.html',
        context_instance=RequestContext(request)
    )
    response.status_code = 404
    return response


def learned(request):
    """Stub."""
    return render_to_response('learned.html', {})
