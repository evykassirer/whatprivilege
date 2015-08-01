"""Helper functions for whatprivilege app view logic."""
from whatprivilege.models import Question, Answer


def get_next_question(previous=0):
    """
    Given the user's previously answered question id [if there is one], return
    the next question to be answered.
    """
    question = None
    question = Question.objects.filter(id__gt=previous).order_by('pk').first()
    return question


def calculate_percent_no(yes, no):
    """
    Calculates the percentage of people who answered no
    out of the total (yes + no).
    """
    if yes + no == 0:
        return 0
    return int(round(
        float(no) / float(yes + no),
        2
    ) * 100)


def get_percent_no(question):
    """
    Gets the percentage of people who answered no to a given question.
    """
    return calculate_percent_no(
        Answer.objects.filter(
            yes=True, question=question).count(),
        Answer.objects.filter(
            yes=False, question=question).count()
    )


def get_question_total():
    """
    Get the total number of questions the user has access to.
    """
    return Question.objects.count() or 1


def get_question_number(id):
    """
    Get the current question number that the user is seeing, as in they are on
    'Question (number)/(Total)'
    """
    return Question.objects.filter(id__lt=id).count() + 1

def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None
