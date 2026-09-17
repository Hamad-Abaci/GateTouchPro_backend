from django.contrib import admin
from .models import Lane,AccessLog,TurnStyle,SystemConfig
admin.site.register(Lane)
admin.site.register(AccessLog)
admin.site.register(TurnStyle)
admin.site.register(SystemConfig)