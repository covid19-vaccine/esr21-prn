from django.apps import apps as django_apps
from django.db import models
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import date_not_before_study_start
from edc_protocol.validators import datetime_not_before_study_start
from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from edc_action_item.model_mixins import ActionModelMixin

from ..action_items import SUBJECT_OFFSTUDY_ACTION
from ..choices import OFF_STUDY_REASON


class SubjectOffstudy(OffScheduleModelMixin, ActionModelMixin, BaseUuidModel):

    """ A model completed by the user that completed when the subject is taken
        off-study.
    """

    tracking_identifier_prefix = 'OS'

    action_name = SUBJECT_OFFSTUDY_ACTION

    offstudy_date = models.DateField(
        verbose_name='Date of completion or discontinuation',
        null=True,
        default=get_utcnow,
        validators=[
            date_not_before_study_start,
            date_not_future])

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        null=True,
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    completed_study = models.CharField(
        verbose_name='Did the subject complete the study?',
        max_length=3,
        choices=YES_NO)

    reason = models.CharField(
        verbose_name='No, primary reason for early discontinuation',
        max_length=115,
        choices=OFF_STUDY_REASON,
        blank=True,
        null=True)

    reason_other = OtherCharField()

    death_date = models.DateField(
        verbose_name='Date of death',
        blank=True,
        null=True,
        help_text='(derived, no entry required)')

    comment = models.TextField(
        max_length=250,
        verbose_name='Comment',
        blank=True,
        null=True)

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.consent_version = None
        super(SubjectOffstudy, self).save(*args, **kwargs)

    def take_off_schedule(self):
        on_schedule = django_apps.get_model('esr21_subject.onschedule')

        _, schedule = site_visit_schedules.get_by_onschedule_model(
            onschedule_model=on_schedule._meta.label_lower)
        schedule.take_off_schedule(offschedule_model_obj=self)

    class Meta:
        app_label = 'esr21_prn'
        verbose_name_plural = 'Subject Off Study'
