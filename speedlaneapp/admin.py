from django.contrib import admin
from .models import Lane,AccessLog,TurnStyle,SystemConfig,LaneGroup,User
admin.site.register(User)
admin.site.register(Lane)
admin.site.register(LaneGroup)
admin.site.register(AccessLog)
admin.site.register(TurnStyle)
admin.site.register(SystemConfig)