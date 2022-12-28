from django.apps import AppConfig

class NewusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newusers'

    def ready(self):
        pass