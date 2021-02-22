from django.contrib import admin

from .models import Auther, Contact, Quote

admin.site.register(Auther)

admin.site.register(Quote)
admin.site.register(Contact)
