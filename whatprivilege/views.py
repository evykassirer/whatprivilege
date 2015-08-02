"""All request-handling logic for whatprivilege app."""
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from whatprivilege.models import Question, Answer, Visitor
from whatprivilege.helpers import (
    get_next_question, get_question_number,
    get_question_total, get_percent_no, get_or_none)


def show_results(request):
    """
    Displays the results page
    """
    questions = Question.objects.all().order_by('position')

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
    if 'show_results' in request.COOKIES.keys() and (
            request.COOKIES['show_results'] == 'yes'):
        return show_results(request)

    current_q = None
    visitor = None
    new_visitor = False

    if request.method == 'POST':
        # The user has submitted an answer to a question.
        # Get User ID
        if 'visitor' in request.COOKIES.keys():
            visitor = Visitor.objects.get(id=request.COOKIES['visitor'])
        else:   # if this is a new visitor
            visitor = Visitor()
            visitor.save()
            new_visitor = True

        is_yes = request.POST.get("yesno") == 'yes'
        is_skip = request.POST.get("yesno") not in ("yes", "no")
        current_q = Question.objects.get(
                id=request.POST.get("qnumber"))
        if not Answer.objects.filter(
                question=current_q.id, visitor=visitor
                ).exists() and not is_skip:
            # The user has not answered this question yet. Count the response.
            answer = Answer(yes=is_yes, question=current_q, visitor=visitor)
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
        if new_visitor:
            response.set_cookie("visitor", visitor.id)
        return response

    else:
        # We have iterated through all questions.
        # Set a cookie for question completion and display the results page.
        response = show_results(request)
        response.set_cookie('show_results', 'yes')
        if new_visitor:
            response.set_cookie("visitor", visitor.id)
        return response


def feedback(request):
    """A form for the user to submit feedback to the developers, sent via email.
    """
    if request.method == 'POST':
        # the user has just submitted feedback, send email
        content = request.POST.get("feedback")
        email = request.POST.get("email")
        name = request.POST.get("name")
        content = content + "\n\nThis email was sent from: " + name + \
                            "\n\nYou can reply to this person at: " + email
        send_mail('**FEEDBACK FROM WHATPRIVILEGE**', content, email,
                  ['evy.kassirer@gmail.com'], fail_silently=False)
        return render_to_response('thankyou.html')

    # otherwise, load the form
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

def discussion(request):
    q_id = request.GET.get("id")
    question = get_or_none(Question, id=q_id)
    if not question:
        return redirect('/')
    percent_no = get_percent_no(question)
    context = {
        # maybe have another field that's a negation like 23% of users "cannot walk home feeling safe"
        'question': question,
        'percent_no': percent_no,
        'current_path': request.build_absolute_uri(),
    }
    return render_to_response(
        'discussion.html',
        RequestContext(request, context))
