from django import forms
from recipebox.models import Author


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.CharField(max_length=15)
    instructions = forms.CharField(widget=forms.Textarea)