from django import forms

class MovieSearchForm(forms.Form):
    query = forms.CharField(label='Search Movies', max_length=100)