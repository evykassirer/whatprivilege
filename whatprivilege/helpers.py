"""Helper functions for whatprivilege app view logic."""
from whatprivilege.models import Question, Answer


def get_next_question(previous=0, workshop=None):
    """
    Given the user's previously answered question id [if there is one], return
    the next question to be answered.
    """
    question = None
    if workshop:
        question = Question.objects.filter(
                id__gt=previous, workshops=workshop).order_by('pk').first()
    else:
        question = Question.objects.filter(
                id__gt=previous, workshop_only=False).order_by('pk').first()
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


def get_percent_no(question, workshop=None):
    """
    Gets the percentage of people who answered no to a given question
    [within a given workshop].
    """
    if workshop:
        return calculate_percent_no(
            Answer.objects.filter(
                yes=True, question=question, workshop=workshop).count(),
            Answer.objects.filter(
                yes=False, question=question, workshop=workshop).count()
        )
    return calculate_percent_no(
        Answer.objects.filter(
            yes=True, question=question).count(),
        Answer.objects.filter(
            yes=False, question=question).count()
    )


def get_question_total(workshop=None):
    """
    Get the total number of questions the user has access to
    [within a given workshop]
    """
    if workshop:
        return Question.objects.filter(workshops=workshop).count() or 1
    return Question.objects.filter(workshop_only=False).count() or 1


def get_question_number(id, workshop=None):
    """
    Get the current question number that the user is seeing, as in they are on
    'Question (number)/(Total)' [within a given workshop].
    """
    if workshop:
        return Question.objects.filter(
            workshops=workshop, id__lt=id).count() + 1
    return Question.objects.filter(workshop_only=False, id__lt=id).count() + 1
