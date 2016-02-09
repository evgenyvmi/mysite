from django.contrib import admin

from .models import Research_interests
from .models import Request
from .models import Expert

# Register your models here.

admin.site.register(Research_interests)
admin.site.register(Request)
admin.site.register(Expert)
