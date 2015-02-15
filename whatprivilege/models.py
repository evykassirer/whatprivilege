from django.db import models

class Question(models.Model):
	questionText=models.TextField()
	helpText=models.TextField()
	helpLink=models.URLField()
	numberYes=models.IntegerField()
	numberNo=models.IntegerField()

class Workshop(models.Model):
	urlCode=models.TextField()

class WorkshopQuestion(models.Model):
	workshopID=models.IntegerField()
	qID=models.IntegerField()
	numberYes=models.IntegerField()
	numberNo=models.IntegerField()