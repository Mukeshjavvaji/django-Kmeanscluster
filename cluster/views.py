from django.shortcuts import render
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
from .forms import DataForm
import pandas as pd

# Create your views here.
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error": "0",
        "message": "Successful"
    }
    return Response(return_data)

@api_view(["POST"])
def predict(request):
    form = DataForm(request.POST)
    if form.is_valid():
        race = int(form.cleaned_data['race'])
        gender = int(form.cleaned_data['gender'])
        discharge_disposition_id = form.cleaned_data['discharge_disposition_id']
        admission_source_id = form.cleaned_data['admission_source_id']
        time_in_hospital = form.cleaned_data['time_in_hospital']
        num_lab_procedures = form.cleaned_data['num_lab_procedures']
        num_procedures = form.cleaned_data['num_procedures']
        num_medications = form.cleaned_data['num_medications']
        number_outpatient = form.cleaned_data['number_outpatient']
        number_emergency = form.cleaned_data['number_emergency']
        number_inpatient = form.cleaned_data['number_inpatient']
        diag_3 = form.cleaned_data['diag_3']
        number_diagnoses = form.cleaned_data['number_diagnoses']
        max_glu_serum = int(form.cleaned_data['max_glu_serum'])
        A1Cresult = int(form.cleaned_data['A1Cresult'])
        metformin = int(form.cleaned_data['metformin'])
        repaglinide = int(form.cleaned_data['repaglinide'])
        pioglitazone = int(form.cleaned_data['pioglitazone'])
        glipizide_metformin = int(form.cleaned_data['glipizide_metformin'])
        change = int(form.cleaned_data['change'])
        diabetesMed = int(form.cleaned_data['diabetesMed'])
        data_point = {'race' : race, 'gender' : gender, 'discharge_disposition_id': discharge_disposition_id, 'admission_source_id': admission_source_id, 'time_in_hospital': time_in_hospital, 'num_lab_procedures': num_lab_procedures, 'num_procedures' : num_procedures, 'num_medications': num_medications, 'number_outpatient': number_outpatient, 'number_emergency': number_emergency, 'number_inpatient': number_inpatient, 'diag_3': diag_3, 'number_diagnoses': number_diagnoses, 'max_glu_serum': max_glu_serum, 'A1Cresult': A1Cresult, 'metformin': metformin, 'repaglinide': repaglinide, 'pioglitazone': pioglitazone, 'glipizide_metformin': glipizide_metformin, 'change' : change, 'diabetesMed': diabetesMed}
        df = pd.DataFrame(data_point, index=[0])
        cluster_model = pickle.load(open("D:\Internships\HotNot\Assignment\TRAIN\cluster_model.sav", "rb"))
        output = cluster_model.predict(df)
        message = {0: 'The patient is not required to readmit', 1:'The patient is required to readmit'}
        return render(request, 'result.html', {'message': message[output[0]]})
    else:
        print(form.errors)

def open_form(request):
    return render(request, 'index.html', {'form': DataForm})

# def status(df):
