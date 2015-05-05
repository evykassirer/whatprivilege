from django.db import models
from django.conf import settings
from hashlib import sha256

class Question(models.Model):
    """
    A question to ask the user.
    """
    text = models.TextField()
    help_text = models.TextField(blank=True)
    help_link = models.URLField(blank=True)
    
    def __unicode__(self):
        """Make Django print the question's text whenever possible (including
        on the /admin/ page)."""
        return u'%s' % self.text


class AnswerTally(models.Model):
    """
    Answers to a question in terms of number responses that are 'yes' or 'no'.
    """

    num_yes = models.IntegerField(default=0)
    num_no = models.IntegerField(default=0)
    question = models.ForeignKey('Question')

    def __unicode__(self):
        """Make Django print the answer's type whenever possible (including on
        the /admin/ page)."""
        text = str(self.question) + ' ' + '#yes %d ' % self.num_yes + ' ' + '#no %d' %self.num_no
        return text
