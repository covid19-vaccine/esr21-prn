from django.db import models

from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO

from ..action_items import DEATH_REPORT_ACTION
from ..choices import CAUSE_OF_DEATH, CAUSE_OF_DEATH_CAT, MED_RESPONSIBILITY
from ..choices import HOSPITILIZATION_REASONS


class DeathReport(SiteModelMixin, ActionModelMixin, BaseUuidModel):

    action_name = DEATH_REPORT_ACTION

    tracking_identifier_prefix = 'DR'

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    death_date = models.DateField(
        verbose_name='Death date',
        default=get_utcnow, )

    cause_of_death = models.CharField(
        verbose_name='What is the primary source of cause of death '
                     'information?',
        max_length=50,
        choices=CAUSE_OF_DEATH,)

    cause_of_death_other = models.CharField(
        verbose_name='Other, specify',
        max_length=50,)

    perform_autopsy = models.CharField(
        verbose_name='Will an autopsy be performed later',
        max_length=20,
        choices=YES_NO,)

    major_cause_of_death = models.TextField(
        verbose_name='Describe the major cause of death (including pertinent '
                     'autopsy information if available), starting with the '
                     'first noticeable illness thought to be related to '
                     'death, continuing to time of death.',
        max_length=50,
        help_text='(Note: Cardiac and pulmonary arrest are not major reasons '
                  'and should not be used to describe major cause) ')

    description = models.CharField(
        verbose_name='Based on the description above, what category best'
                     'defines the major cause of death?',
        max_length=50,
        choices=CAUSE_OF_DEATH_CAT,)

    description_other = models.CharField(
        verbose_name='Other, specify',
        max_length=50,)

    duration_acute_illness = models.IntegerField(
        verbose_name='Duration of acute illness directly causing death',
        help_text='(in days (If unknown enter -1))')

    medical_responsibility = models.CharField(
        choices=MED_RESPONSIBILITY,
        max_length=50,
        verbose_name=('Who was responsible for primary medical care of the '
                      'participant during the month prior to death?'))

    participant_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Was the participant hospitalised before death?')

    reason_participant_hospitalized = models.CharField(
        max_length=65,
        choices=HOSPITILIZATION_REASONS,
        verbose_name='Was the participant hospitalised before death?')

    reason_participant_hospitalized_other = models.CharField(
        verbose_name='If other illness or pathogen specify or non '
                     'infectious reason, please specify',
        max_length=50,)

    period_hospitalized = models.IntegerField(
        verbose_name='For how many days was the participant hospitalised '
                     'during the illness immediately before death?',)

    comments = models.TextField(
        verbose_name='Comments',)

    class Meta:
        app_label = 'esr21_prn'
        verbose_name = 'Death Report'
        verbose_name_plural = 'Death Report'
