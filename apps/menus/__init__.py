from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class Menus(AppConfig):
    name = 'apps.menus'
    verbose_name = _('Menus')

    def ready(self):
        pass
