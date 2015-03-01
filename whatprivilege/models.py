from django.db import models
from django.conf import settings
from hashlib import sha256


class Workshop(models.Model):
    """
    A custom grouping of questions and response data accessed by a custom URL.
    This enables custom group sessions to be run and analyzed.
    """
    code = models.CharField(blank=True, null=True, max_length=255)
    title = models.TextField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True, max_length=255)

    def add_default_questions(self):
        """Adds generic, non-workshop-specific questions."""
        for question in Question.objects.filter(workshop_only=False):
            if self not in question.workshops.all():
                self.questions.add(question)

    def set_code(self):
        """Generates a unique code, to be used in a custom URL."""
        self.code = sha256(settings.SECRET_KEY + str(self.pk)).hexdigest()

    def setup(self):
        """How we want to set up a workshop by default."""
        self.set_code()
        self.add_default_questions()
        self.save()

    def __unicode__(self):
        """Make Django print the Workshop's details whenever possible (including
        on the /admin/ page)."""
        if self.title:
            return self.title
        return 'Workshop %d' % self.id


class Question(models.Model):
    """
    A question to ask the user.
    """
    text = models.TextField()
    helpText = models.TextField(blank=True)
    helpLink = models.URLField(blank=True)
    workshops = models.ManyToManyField(
        Workshop,
        related_name='questions',
        blank=True,
        null=True
    )
    workshop_only = models.BooleanField(default=False)

    def __unicode__(self):
        """Make Django print the question's text whenever possible (including
        on the /admin/ page)."""
        return u'%s' % self.text


class Answer(models.Model):
    """
    Answers a question as 'yes' or 'no'.
    Can reference an optional Workshop to be kept track of by individual
    workshops.
    """
    def _no(self):
        """Returns whether or not the answer is no."""
        return not self.yes

    yes = models.BooleanField()
    no = property(_no)
    question = models.ForeignKey('Question')
    workshop = models.ForeignKey('Workshop',  # Let this field be empty.
                                 null=True, blank=True, default=None)

    def __unicode__(self):
        """Make Django print the answer's type whenever possible (including on
        the /admin/ page)."""
        text = str(self.question) + ' '
        text += 'Yes' if self.yes else 'No'
        if self.workshop:
            text += ' (Workshop ID %d)' % self.workshop.id
        return text
