from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """Model representing an Product."""
    name = models.CharField(_("name"), max_length=200)
    price = models.FloatField(_("price"))

    class Meta:
        ordering = ['name', 'price']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.name}, {self.price}"


class Customer(models.Model):
    """Model representing an customer."""
    name = models.CharField(_("name"), max_length=200)
    city = models.ForeignKey("City", on_delete=models.SET_NULL, null=True)
    # Foreign Key used because customer can only have one city, but city can have multiple customer
    # Author as a string rather than object because it hasn't been declared yet in file.
    product = models.ManyToManyField(Product, verbose_name=_("product"),
                                     help_text=_("Select a product for this customer"))
    # ManyToManyField used because a product can contain many customers and a Customer can cover many products.
    # Genre class has already been defined so we can specify the object above.
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['city', '-timestamp']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.name}, {self.city}, {self.product.name}"


class City(models.Model):
    """Model representing an City."""
    name = models.CharField(_("name"), max_length=200)
    number_inhabitants = models.CharField(_("number_inhabitants"), max_length=100)

    class Meta:
        ordering = ['name', 'number_inhabitants']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.name}, {self.number_inhabitants}"


class Provider(models.Model):
    """Model representing an provider."""
    city = models.OneToOneField("City", on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.name}, {self.city.name}"

#  python3 manage.py graph_models polls  > my_project.dot
