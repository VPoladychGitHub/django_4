from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Log_midlware(models.Model):
    """Model representing an person."""
    path = models.CharField(_("path"), max_length=200)
    method = models.CharField(_("method"), max_length=100)
    timestamp = models.FloatField(_("timestamp"))

    class Meta:
        ordering = ['-timestamp', 'method', 'path']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.path}, {self.method}, {self.timestamp}"


class Person(models.Model):
    """Model representing an person."""
    first_name = models.CharField(_("first_name"), max_length=200)
    last_name = models.CharField(_("last_name"), max_length=100)
    email = models.CharField(_("email"), max_length=100)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.first_name}, {self.last_name}, {self.email}"

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('person-create')
