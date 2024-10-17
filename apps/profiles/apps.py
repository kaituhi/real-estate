from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.profiles"

    def ready(self):
        """
        This method is called when the app is ready.
        Importing signals here ensures they are registered
        """
        from apps.profiles import signals
