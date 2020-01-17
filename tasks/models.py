""" Tasks Models """

from django.db import models
from users.models import User

class Task(models.Model):
	""" Tasks model """
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	cDate = models.DateField(verbose_name="Created date")
	fDate = models.DateField(verbose_name="Finished date")
	description = models.TextField(max_length=500)

class SubTask(models.Model):
	""" Tasks model """
	father = models.ForeignKey(Task,on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	cDate = models.DateField(verbose_name="Created date")
	fDate = models.DateField(verbose_name="Finished date")
	description = models.TextField(max_length=500)