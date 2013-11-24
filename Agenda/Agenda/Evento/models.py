from django.db import models

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length = 30)
	description = models.CharField(max_length = 30)
	creation_date = models.DateField()
	start_date = models.DateField()
	end_date = models.DateField()
	userid = models.IntegerField()
	status = models.CharField(max_length = 1)

	def __str__(self):
		return self.name
