from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style

style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'esr21_prn'
    verbose_name = 'ESR21 PRN'
    admin_site_name = 'esr21_prn_admin'
