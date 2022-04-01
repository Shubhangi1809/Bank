from django.apps import AppConfig


class BdmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BDMS'

    def ready(self):
        import BDMS.signals
