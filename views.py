from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, 'home.html')

def crop_prediction(request):
    return render(request, 'crop_prediction.html')

def fertilizer_prediction(request):
    return render(request, 'fertilizer_prediction.html')

def crop_result(request):

    model = joblib.load("finalized_crop_Recommendation_model.sav")
    input_list = []
    input_list.append(request.GET['N'])
    input_list.append(request.GET['P'])
    input_list.append(request.GET['K'])
    input_list.append(request.GET['temperature'])
    input_list.append(request.GET['humidity'])
    input_list.append(request.GET['ph'])
    input_list.append(request.GET['rainfall'])
    # print(input_list)
    input_list_num = list(map(float, input_list))
    prediction = model.predict([input_list_num])
    return render(request, 'crop_result.html', {'prediction': prediction})

def fertilizer_result(request):

    model = joblib.load("finalized_fertilizer_prediction_model.sav")
    input_list = []
    input_list.append(request.GET['temperature'])
    input_list.append(request.GET['humidity'])
    input_list.append(request.GET['moisture'])
    input_list.append(request.GET['soil_type'])
    input_list.append(request.GET['crop_type'])
    input_list.append(request.GET['N'])
    input_list.append(request.GET['P'])
    input_list.append(request.GET['K'])
    # print(input_list)
    prediction = model.predict([input_list])
    return render(request, 'fertilizer_result.html', {'prediction': prediction})