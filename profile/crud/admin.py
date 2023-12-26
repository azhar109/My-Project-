from django.contrib import admin
from .models.apply import Apply
from .models.professor import Professor

# Register your models here.

admin.site.register(Apply)
admin.site.register(Professor)

