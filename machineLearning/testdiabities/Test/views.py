from django.shortcuts import render
from django.http import HttpResponse
from pycaret.datasets import get_data
from pycaret.classification import *
from pycaret.classification import ClassificationExperiment
from pycaret.classification import load_model, predict_model
import pandas as pd
import numpy as np
from . import *
import os
from django.conf import settings  # Import Django's settings module
def index(request):
    
    return render(request,'index.html')

def test(request):
    
    model_path = os.path.join(settings.BASE_DIR, 'Test/my_best_pipeline')

    # Load the model
    loaded_model = load_model(model_path)

    arr = np.array([
            int(request.POST.get("one")),
            float(request.POST.get("two")),
            float(request.POST.get("three")),
            float(request.POST.get("four")),
            float(request.POST.get("five")),
            float(request.POST.get("six")),
            float(request.POST.get("seven")),
            int(float(request.POST.get("eight")))
        ])

    columns = [
            "Number of times pregnant",
            "Plasma glucose concentration a 2 hours in an oral glucose tolerance test",
            "Diastolic blood pressure (mm Hg)",
            "Triceps skin fold thickness (mm)",
            "2-Hour serum insulin (mu U/ml)",
            "Body mass index (weight in kg/(height in m)^2)",
            "Diabetes pedigree function",
            "Age (years)",
        ]

    data1 = pd.DataFrame([arr], columns=columns)

        # Make predictions using the loaded model
    predictions = predict_model(loaded_model, data=data1)
        
        # Access the predicted class and score
    predicted_class = predictions['prediction_label'][0]
    predicted_score = predictions['prediction_score'][0]

    context = {
    'predicted_class': predicted_class,
    'predicted_score': predicted_score
    }

    

    return render(request,'predict.html',context)
