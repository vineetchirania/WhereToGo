from django import forms
from data_interface import fetch_activities_from_db

class ActivityForm(forms.Form):
    OPTIONS = fetch_activities_from_db()
    Activities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
