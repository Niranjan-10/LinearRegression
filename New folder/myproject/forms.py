from django import forms

mylist = ['Yes', 'No']
class MyForm(forms.Form):
    GRE_score = forms.FloatField(required=True)
    TOEFL_score = forms.FloatField(required=True)
    University_rating = forms.IntegerField(required=True,max_value=5)
    SOP = forms.FloatField(required=True)
    LOR = forms.FloatField(required=True)
    CGPA = forms.FloatField(required=True)
    Research = forms.ChoiceField(choices=[(i,i) for i in mylist])
