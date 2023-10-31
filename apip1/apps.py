from django.apps import AppConfig

class Apip1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apip1'

    def ready(self) -> None:
        from .signals import log_changes
        return super().ready()  

