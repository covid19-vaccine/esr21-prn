from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy

from edc_sync.tests import SyncTestHelper


@tag('sync')
class TestNaturalKey(TestCase):

    sync_test_helper = SyncTestHelper()

    def setUp(self):
        import_holidays()

        self.eligibility_confirmation = mommy.make_recipe(
            'esr21_subject.eligibilityconfirmation')

        self.options = {
            'screening_identifier': self.eligibility_confirmation.screening_identifier,
            'consent_datetime': get_utcnow() - relativedelta(days=5),
            'version': '1'}

        self.informed_consent = mommy.make_recipe(
            'esr21_subject.informedconsent',
            **self.options)

        self.screening_options = {
            'subject_identifier': self.informed_consent.subject_identifier}

        self.screening_eligibility = mommy.make_recipe(
            'esr21_subject.screeningeligibility',
            **self.screening_options)

    def test_natural_key_attrs(self):
        self.sync_test_helper.sync_test_natural_key_attr('esr21_prn')

    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr('esr21_prn')
