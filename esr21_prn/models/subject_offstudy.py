from django.db import models
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future, datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import (
    date_not_before_study_start, datetime_not_before_study_start)

from ..action_items import SUBJECT_OFFSTUDY_ACTION


class SubjectOffStudy(ActionModelMixin, BaseUuidModel):

    action_name = SUBJECT_OFFSTUDY_ACTION

    tracking_identifier_prefix = 'SO'

    subject_identifier = models.CharField(
        max_length=50,
        unique=True)

    scheduled_data = models.CharField(
        verbose_name='Are scheduled data being submitted on the exit date?',
        max_length=3,
        choices=YES_NO,)

    offstudy_date = models.DateField(
        verbose_name='Offstudy date',
        null=True,
        default=get_utcnow,
        validators=[date_not_before_study_start, date_not_future],)

    report_datetime = models.DateTimeField(
        verbose_name='Report datetime',
        validators=[datetime_not_before_study_start, datetime_not_future],
        null=True,
        default=get_utcnow,)

    reason = models.CharField(
        verbose_name='Reason for exit',
        max_length=50,
        null=True,)

    reason_other = OtherCharField()

    general_comments = models.TextField(
        verbose_name='Any general comments about patient exit?',
        max_length=150,
        blank=True,
        null=True)

    last_visit_date = models.DateField(
        verbose_name='What was the date of patient\'s last visit?',
        validators=[date_not_future, ],)

    last_visit_facility_other = OtherCharField()

    def natural_key(self):
        return (self.subject_identifier)

    natural_key.dependencies = ['sites.Site']

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.consent_version = None
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'esr21_prn'
        verbose_name = 'Subject off Study'
        verbose_name_plural = 'Subject Off Study'
