import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	def __str__(self):              # __unicode__ on Python 2
		return self.question_text
	def was_published_recently(self):
		return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):              # __unicode__ on Python 2
		return self.choice_text

