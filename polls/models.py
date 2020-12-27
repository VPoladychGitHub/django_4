import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    """Model representing an person."""
    username = models.CharField(_("username"), max_length=200)
    email = models.CharField(_("email"), max_length=100)
    password = models.CharField(_("password"), max_length=100)

    class Meta:
        ordering = ['username', 'email']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.username}, {self.email}"
