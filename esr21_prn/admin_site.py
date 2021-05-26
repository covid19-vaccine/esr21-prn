from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_url = '/administration/'
    enable_nav_sidebar = False
    site_header = 'ESR21 PRN'
    site_title = 'ESR21 PRN'
    index_title = 'ESR21 PRN'


esr21_prn_admin = AdminSite(name='esr21_prn_admin')
