from django.apps import AppConfig


class InpatientsystemappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inpatientsystemApp'

    def ready(self):
        import inpatientsystemApp.signals