from django.contrib import admin

from .models import Provider, Product, City, Customer

admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(City)
admin.site.register(Customer)
