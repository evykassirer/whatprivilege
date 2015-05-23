from django.contrib import admin
from whatprivilege.models import Question, Answer, Visitor
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Visitor)