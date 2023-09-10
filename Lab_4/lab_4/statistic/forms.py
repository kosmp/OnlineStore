from django import forms

class StatisticForm(forms.Form):
    schedule = forms.ImageField()

    class META:
        fields = ['schedule']