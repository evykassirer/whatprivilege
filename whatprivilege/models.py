from django.db import models
from django.conf import settings
from hashlib import sha256

class Question(models.Model):
    """
    A question to ask the user.
    """
    # position determines the order in which questions are asked
    position = models.IntegerField()
    text = models.TextField()
    help_text = models.TextField(blank=True)
    help_link = models.URLField(blank=True)
    
    def __unicode__(self):
        """Make Django print the question's text whenever possible (including
        on the /admin/ page)."""
        return u'%s' % self.text


class Answer(models.Model):
    """
    Answer to a question as 'yes' or 'no'.
    """

    def _no(self):
        """Returns whether or not the answer is no."""
        return not self.yes

    yes = models.BooleanField(default=False)
    no = property(_no)
    question = models.ForeignKey('Question')
    visitor = models.ForeignKey('Visitor')
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """Make Django print the answer's type whenever possible (including on
        the /admin/ page)."""
        text = str(self.question) + ' '
        text += 'Yes' if self.yes else 'No'
        return text

class Visitor(models.Model):
    """
    A visitor to the application, whose answers are associated with the unique key of this object
    """