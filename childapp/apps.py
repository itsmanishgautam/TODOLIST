from django.apps import AppConfig


class ChildappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'childapp'
