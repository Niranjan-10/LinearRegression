from django.shortcuts import render,redirect
from .forms import MyForm
import pickle
import os
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
# @csrf_exempt
def linearRegression(request):
    # file = os.path.join(settings.BASE_DIR, 'myfinal_linearregression.pickle')
    # print(file)
    # print(request.POST)
    if request.method == 'POST':
        # print(request.POST)
        form = MyForm(request.POST)
        if form.is_valid():
            GRE_score = form.cleaned_data['GRE_score']
            TOEFL_score = form.cleaned_data['TOEFL_score']
            University_rating = form.cleaned_data['University_rating']
            SOP = form.cleaned_data['SOP']
            LOR = form.cleaned_data['LOR']
            CGPA = form.cleaned_data['CGPA']
            Research = form.cleaned_data['Research']

            if Research == 'Yes':
                research = 1
            else:
                research = 0
            print(research)

            result = "{:.2f}".format(calculatePercentage(GRE_score,TOEFL_score,University_rating,SOP,LOR,CGPA,research))
           
            final_result = float(result)*100
            print(final_result)
        #     print('GRE_score')
        # gre_score = request.POST.get('GRE_score')
        # toefl_score = request.POST.get('TOEFL_score')
        # university_rating = request.POST.get('University_rating')
        # sop = request.POST.get('SOP')
        # lor = request.POST.get('LOR')
        # cgpa = request.POST.get('CGPA')
        # research = request.POST.get('Research')
        
            return render(request,'result.html',{'result':final_result})
    else:
        form = MyForm()
    return render(request,'index.html', {'form':form})

def calculatePercentage(gre_score,toefl_score,university_rating,sop,lor,cgpa,research):
    file = os.path.join(settings.BASE_DIR, 'myfinal_linearregression.pickle')
    loaded_model = pickle.load(open(file, 'rb'))
        # print(loaded_model)
    prediction=loaded_model.predict([[float(gre_score),float(toefl_score),float(university_rating),float(sop),float(lor),float(cgpa),int(research)]])
    print(prediction[0])

    return prediction[0]
        

