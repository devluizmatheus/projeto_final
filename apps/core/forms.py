from django import forms

from .models import Enjoyer, Selection, SelectionEnjoyer

class EnjoyerForm(forms.ModelForm):
    class Meta:
        model = Enjoyer
        fields = '__all__'

class SelectionForm(forms.ModelForm):
    class Meta:
        model = Selection
        fields = '__all__'

class SelectionEnjoyerForm(forms.Form):
    class Meta:
        model = SelectionEnjoyer
        fields = '__all__'