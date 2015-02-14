from django.db import models

class Question(models.Model):
	questionText=models.TextField()
	helpText=models.TextField()
	helpLink=models.URLField()
	numberYes=models.IntegerField()
	numberNo=models.IntegerField()

