from django import forms


class FilterForm(forms.Form):
    price_min = forms.IntegerField()
    price_max = forms.IntegerField()
    checks = forms.
