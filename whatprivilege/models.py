from django.db import models

class Question(models.Model):
	questionText=models.TextField()
	helpText=models.TextField()
	helpLink-models.UrlField()
	numberYes=models.IntegerField()
	numberNo=models.IntegerField()

