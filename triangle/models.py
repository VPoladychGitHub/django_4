from django.db import models

from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    """Model representing an Contact."""
    from_email = models.EmailField(_("mail"), default="test@test.com")
    subject = models.CharField(_("subject"), max_length=200)
    message = models.TextField(_("message"), max_length=1000, help_text=_("message"))
    result = models.CharField(_("result"), max_length=100, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.subject, self.message}"


class Auther(models.Model):
    """Model representing an Auther."""
    name = models.CharField(_("name"), max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.name}"


class Quote(models.Model):
    """Model representing an Quote."""
    quote = models.TextField(_("quote"))
    auther = models.ForeignKey("Auther", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.quote}"


class AutherQuote(models.Model):
    """Model representing an Product."""
    name = models.CharField(_("name"), max_length=200)
    quote = models.CharField(_("quote"), max_length=200)

    class Meta:
        ordering = ['name', 'quote']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.name}, {self.quote}"
