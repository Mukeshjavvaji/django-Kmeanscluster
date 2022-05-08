from django import forms
from .models import DataPoint

class DataForm(forms.ModelForm):
    class Meta:
        model = DataPoint
        fields = "__all__"
    
    race = forms.TypedChoiceField(choices=[(2, 'Caucasian'), (0, 'AfricanAmerican'), (-1, 'Hispanic'), (3, 'Other'), (4, 'Asian'), (1, 'None')])
    gender = forms.TypedChoiceField(choices=[(0, 'Male'), (1, 'Female')])
    discharge_disposition_id = forms.IntegerField()
    admission_source_id = forms.IntegerField()
    time_in_hospital = forms.IntegerField()
    num_lab_procedures = forms.IntegerField()
    num_procedures = forms.IntegerField()
    num_medications = forms.IntegerField()
    number_outpatient = forms.IntegerField()
    number_emergency = forms.IntegerField()
    number_inpatient = forms.IntegerField()
    diag_3 = forms.IntegerField()
    number_diagnoses = forms.IntegerField()
    max_glu_serum_choices = [(2, 'None'), (3, 'Norm'), (0, '>200'), (1, '>300')]
    max_glu_serum = forms.TypedChoiceField(choices = max_glu_serum_choices)
    choice = [(1, 'No'), (2, 'Steady'), (3, 'Up'), (0, 'Down')]
    A1Cresult_choices = [(2, 'None'), (1, '>8'), (3, 'Norm'), (0, '>7')]
    A1Cresult = forms.TypedChoiceField(choices = A1Cresult_choices)
    metformin = forms.TypedChoiceField(choices = choice)
    repaglinide = forms.TypedChoiceField(choices = choice)
    pioglitazone = forms.TypedChoiceField(choices = choice)
    glipizide_metformin = forms.TypedChoiceField(choices = choice)
    change = forms.TypedChoiceField(choices = [(1, 'No'), (0, 'Ch')])
    diabetesMed = forms.TypedChoiceField(choices = [(1, 'Yes'), (0, 'No')])