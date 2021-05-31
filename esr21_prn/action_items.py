from edc_action_item import Action, site_action_items, HIGH_PRIORITY

SUBJECT_OFFSTUDY_ACTION = 'submit-subjectoff-study'


class SubjectOffStudyAction(Action):
    name = SUBJECT_OFFSTUDY_ACTION
    display_name = 'Submit Subject Offstudy'
    reference_model = 'esr21_prn.subjectoffstudy'
    admin_site_name = 'esr21_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True


site_action_items.register(SubjectOffStudyAction)
