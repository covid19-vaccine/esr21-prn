from django import forms

from ..models import SubjectOffStudy


class SubjectOffStudyForm(forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectOffStudy
        fields = '__all__'
