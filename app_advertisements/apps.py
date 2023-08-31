from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _



class AppAdvertisementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_advertisements'
    verbose_name = _("Объявления")
