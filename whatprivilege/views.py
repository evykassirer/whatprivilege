"""All request-handling logic for whatprivilege app."""
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail

from whatprivilege.models import Question, AnswerTally
from whatprivilege.helpers import (
    get_next_question, get_question_number,
    get_question_total, get_percent_no)

def show_results(request):
    """
    Displays the results page
    """
    questions = Question.objects.all()

    for question in questions:
        question.percent = get_percent_no(question)

    context = {
        'questions': questions,
    }

    return render_to_response(
                'results.html',
                RequestContext(request, context))

def home(request):
    """
    Main landing page.
    """
    response = render_to_response('home.html')

    # The user has just reset from the results page
    if request.method == 'POST':
        response.set_cookie('show_results', 'no')

    return response


def instructions(request):
    """
    Renders instructions page to brief the user before they start answering
    questions.
    """
    return render_to_response('instructions.html')


def question(request):
    """
    Main survey logic. Renders a question that the user should answer, based on
    the state of the user's cookie.
    """

    # first check if we should be showing the results page instead 
    # (if they have answered all the questions)
    if request.COOKIES.has_key('show_results') and (request.COOKIES['show_results'] == 'yes'):
        return show_results(request)

    current_q = None
    already_answered = False

    if request.method == 'POST':
        # The user has submitted an answer to a question.
        is_yes = request.POST.get("yesno") == 'yes'
        is_skip = request.POST.get("yesno") not in ("yes", "no")
        current_q = Question.objects.get(
                id=request.POST.get("qnumber"))
        already_answered = str(current_q.id) in request.COOKIES
        if not already_answered and not is_skip:
            # The user has not answered this question yet. Count the response.
            answer = AnswerTally.objects.get_or_create(question=current_q)[0]
            if(is_yes):
                answer.num_yes += 1
            else:
                answer.num_no += 1
            answer.save()

    question = get_next_question(current_q.id if current_q else 0)

    if question:
        # Display the new question to the user.
        question_number = get_question_number(question.id)
        question_total = get_question_total()
        context = {
             'question': question,
             'percent_no': get_percent_no(question),
             'question_number': question_number,
             'question_total': question_total,
        }

        response = render_to_response(
                'question.html',
                RequestContext(request, context))
        if not already_answered and current_q:
            response.set_cookie(str(current_q.id), 'answered')
        return response

    else:
        # We have iterated through all questions. 
        # Set a cookie for question completion and display the results page.
        response = show_results(request)
        response.set_cookie('show_results', 'yes')
        if not already_answered and current_q:
            response.set_cookie(str(current_q.id), 'answered')
        return response

def feedback(request):
    """A form for the user to submit feedback to the developers, sent via email."""
    if request.method == 'POST':
        #the user has just submitted feedback, send email
        content = request.POST.get("feedback")
        email = request.POST.get("email")
        name = request.POST.get("name")
        content = content + "\n\nThis email was sent from: " + name + \
                            "\n\nYou can reply to this person at: " + email
        send_mail('**FEEDBACK FROM WHATPRIVILEGE**', content, email,
            ['evy.kassirer@gmail.com'], fail_silently=False)
        return render_to_response('thankyou.html') 

    #otherwise, load the form
    return render_to_response('feedback.html', RequestContext(request, {}))


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
