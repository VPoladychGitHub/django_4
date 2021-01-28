from django.db import models

from django.utils.translation import gettext_lazy as _


class AutherQuote(models.Model):
    """Model representing an Product."""
    name = models.CharField(_("name"), max_length=200)
    quote = models.CharField(_("quote"), max_length=200)

    class Meta:
        ordering = ['name', 'quote']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.name}, {self.quote}"

