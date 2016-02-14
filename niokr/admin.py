from django.contrib import admin

from .models import Research_interests
from .models import Request
from .models import Expert
from .models import Client
# Register your models here.

admin.site.register(Research_interests)
admin.site.register(Request)
admin.site.register(Expert)
admin.site.register(Client)
