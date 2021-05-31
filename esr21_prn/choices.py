from edc_constants.constants import OTHER


CAUSE_OF_DEATH = (
    ('autopsy', 'Autopsy'),
    ('clinical_records', 'Clinical records'),
    ('information',
     'Information from study care taker staff prior participant death'),
    ('contact',
     'Contact with other (non-study) physician/nurse/other health care '
     'provider'),
    ('death_certificate', 'Death Certificate'),
    ('participants_relatives', 'Information from participants relatives or '
                               'friends Obituary'),
    ('information_requested', 'Information requested, still pending'),
    ('no_information', 'No information will ever be available'),
    (OTHER, 'Other'),
)

CAUSE_OF_DEATH_CAT = (
    ('study_drug', 'Toxicity from Study Drug'),
    ('non_study_drug', 'Toxicity from non-Study drug'),
    ('trauma', 'Trauma/Accident'),
    ('no_info', 'No information available'),
    (OTHER, 'Other, specify'),
)

HOSPITILIZATION_REASONS = (
    ('respiratory illness(unspecified)', 'Respiratory Illness(unspecified)'),
    ('respiratory illness, cxr confirmed',
     'Respiratory Illness, CXR confirmed'),
    ('respiratory illness, cxr confirmed, bacterial pathogen, specify',
     'Respiratory Illness, CXR confirmed, bacterial pathogen, specify'),
    ('respiratory illness, cxr confirmed, tb or probable tb',
     'Respiratory Illness, CXR confirmed, TB or probable TB'),
    ('diarrhea illness(unspecified)', 'Diarrhea Illness(unspecified)'),
    ('diarrhea illness, viral or bacterial pathogen, specify',
     'Diarrhea Illness, viral or bacterial pathogen, specify'),
    ('sepsis(unspecified)', 'Sepsis(unspecified)'),
    ('sepsis, pathogen specified, specify',
     'Sepsis, pathogen specified, specify'),
    ('mengitis(unspecified)', 'Mengitis(unspecified)'),
    ('mengitis, pathogen specified, specify',
     'Mengitis, pathogen specified, specify'),
    ('non-infectious reason for hospitalization, specify',
     'Non-infectious reason for hospitalization, specify'),
    (OTHER, 'Other infection, specify'),
)

MED_RESPONSIBILITY = (
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('traditional', 'Traditional Healer'),
    ('all', 'Both Doctor or Nurse and Traditional Healer'),
    ('none', 'No known medical care received (family/friends only)'),
)

OFF_STUDY_REASON = (
    ('death', 'Death'),
    ('ltfu', 'Lost to follow up'),
    ('sponsor_terminated', 'Study terminated by sponsor'),
    ('subject_withdrawal', 'Withdrawal by subject'),
    ('pregnancy', 'Pregnancy'),
    ('adverse_event', 'Adverse Event'),
    (OTHER, 'Other, specify'),
)
