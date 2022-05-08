from django.db import models

# Create your models here.
class DataPoint(models.Model):
    race_choices = (('2', 'Caucasian'), ('0', 'AfricanAmerican'), ('-1', 'Hispanic'), ('3', 'Other'), ('4', 'Asian'), ('1', 'None'))
    race = models.CharField(max_length = 2, choices = race_choices)
    gender_choices = (('0', 'Male'), ('1', 'Female'))
    gender = models.CharField(max_length = 1, choices = gender_choices)
    discharge_disposition_id = models.IntegerField()
    admission_source_id = models.IntegerField()
    time_in_hospital = models.IntegerField()
    num_lab_procedures = models.IntegerField()
    num_procedures = models.IntegerField()
    num_medications = models.IntegerField()
    number_outpatient = models.IntegerField()
    number_emergency = models.IntegerField()
    number_inpatient = models.IntegerField()
    diag_3 = models.IntegerField()
    number_diagnoses = models.IntegerField()
    max_glu_serum_choices = (('2', 'None'), ('3', 'Norm'), ('0', '>200'), ('1', '>300'))
    max_glu_serum = models.CharField(max_length = 1, choices = max_glu_serum_choices)
    choice = (('1', 'No'), ('2', 'Steady'), ('3', 'Up'), ('0', 'Down'))
    A1Cresult_choices = (('2', 'None'), ('1', '>8'), ('3', 'Norm'), ('0', '>7'))
    A1Cresult = models.CharField(max_length = 1, choices = A1Cresult_choices)
    metformin = models.CharField(max_length = 1, choices = choice)
    repaglinide = models.CharField(max_length = 1, choices = choice)
    pioglitazone = models.CharField(max_length = 1, choices = choice)
    glipizide_metformin = models.CharField(max_length = 1, choices = choice)
    change = models.CharField(max_length = 1, choices = (('1', 'No'), ('0', 'Ch')))
    diabetesMed = models.CharField(max_length = 1, choices = (('1', 'Yes'), ('0', 'No')))