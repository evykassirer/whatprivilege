from django.contrib import admin
from whatprivilege.models import Question
from whatprivilege.models import WorkshopQuestion
from whatprivilege.models import Workshop
# Register your models here. 

admin.site.register(Question)
admin.site.register(WorkshopQuestion)
admin.site.register(Workshop)