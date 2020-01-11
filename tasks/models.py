""" Tasks Models. """

from django.db import models

class User(models.Model):
	""" User model. """
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	t_first_name = models.CharField(max_length=100)
	t_last_name = models.CharField(max_length=100)
	t_username = models.CharField(max_length=100)
	
	created = models.DateTimeField(auto_now_add=True)