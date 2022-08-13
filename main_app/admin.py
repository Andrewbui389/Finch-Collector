from django.contrib import admin
from .models import Finches, Feeding

# Register your models here.
admin.site.register(Finches)
admin.site.register(Feeding)