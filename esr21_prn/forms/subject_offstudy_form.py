from django import forms
from ..models import SubjectOffstudy


class SubjectOffStudyForm(forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectOffstudy
        fields = '__all__'
