from django.db import models

class Question(models.Model):
	questionText=models.TextField()
	helpText=models.TextField()
	helpLink=models.URLField()
	numberYes=models.IntegerField()
	numberNo=models.IntegerField()

class Instruction(models.Model):
	instructionText=models.TextField()

class Welcome(models.Model):
	welcomeText=models.TextField()

	

