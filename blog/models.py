import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __str__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name


# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	pub_date = models.DateField('date published')
	tags = models.ManyToManyField(Tag)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title

	def get_month(self):
		thedate = self.pub_date
		return thedate.strftime("%B")

	def get_year(self):
		thedate = self.pub_date
		return thedate.strftime("%Y")

