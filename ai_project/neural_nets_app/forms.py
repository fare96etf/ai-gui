from django import forms
from .constants import ACTIVATION_CHOICES

class ChooseDataFormatForm(forms.Form):
    outputs = forms.MultipleChoiceField(label="Choose output fields", required=True, widget=forms.CheckboxSelectMultiple)

    def set_choices(self, choices):
        self.fields["outputs"].choices = choices

class HiddenLayersForm(forms.Form):
    hidden_layers = forms.IntegerField(label="Number of hidden layers", min_value=1)

class HiddenLayerForm(forms.Form):
    neurons = forms.IntegerField(label="Number of neurons", min_value=1, initial=1)
    activation = forms.ChoiceField(label="Activation function", choices=ACTIVATION_CHOICES)