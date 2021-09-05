from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import esr21_prn_admin
from ..forms import SubjectOffStudyForm
from ..models import SubjectOffStudy


@admin.register(SubjectOffStudy, site=esr21_prn_admin)
class SubjectOffStudyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectOffStudyForm

    search_fields = ('subject_identifier',)

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'offstudy_date',
                'completed_study',
                'reason',
                'reason_other',
                'death_date',
                'comment']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'completed_study': admin.VERTICAL,
        'reason': admin.VERTICAL,
    }

    search_fields = ('subject_identifier', )

    list_display = ('subject_identifier', 'offstudy_date', )
