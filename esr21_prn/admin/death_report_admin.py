from django.contrib import admin
from django.db import models
from django.forms import Textarea

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..forms import DeathReportForm
from ..models import DeathReport
from ..admin_site import esr21_prn_admin
from .modeladmin_mixins import ModelAdminMixin


@admin.register(DeathReport, site=esr21_prn_admin)
class DeathReportAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DeathReportForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 500,
                   'cols': 70,
                   'style': 'height: 7em;'})},
    }
    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'report_datetime',
                'death_date',
                'cause_of_death',
                'cause_of_death_other',
                'perform_autopsy',
                'major_cause_of_death',
                'description',
                'description_other',
                'duration_acute_illness',
                'medical_responsibility',
                'participant_hospitalized',
                'reason_participant_hospitalized',
                'reason_participant_hospitalized_other',
                'period_hospitalized',
                'comments',
            ),
        }),
        audit_fieldset_tuple)

    radio_fields = {'cause_of_death': admin.VERTICAL,
                    'perform_autopsy': admin.VERTICAL,
                    'description': admin.VERTICAL,
                    'medical_responsibility': admin.VERTICAL,
                    'participant_hospitalized': admin.VERTICAL,
                    'reason_participant_hospitalized': admin.VERTICAL, }

    list_display = ('subject_identifier', 'death_date')

    search_fields = ('subject_identifier', )
