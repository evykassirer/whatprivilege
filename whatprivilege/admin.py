from django.contrib import admin
from whatprivilege.models import Question, AnswerTally
# Register your models here.

admin.site.register(Question)
admin.site.register(AnswerTally)