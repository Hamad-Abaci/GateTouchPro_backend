from django.apps import AppConfig


class SpeedlineappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'speedlaneapp'

    def ready(self):
        from .lane_trrigger import set_all_pins_off

        set_all_pins_off()