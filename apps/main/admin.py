from django.contrib import admin


from .models import CustomerQueries, Reviews


admin.site.register([CustomerQueries, Reviews])
# Register your models here.
