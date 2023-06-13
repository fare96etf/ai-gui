from django import forms
from .constants import DELIMITERS, ACTIVATION_CHOICES, OPTIMIZERS, LOSSES

class UploadCsvForm(forms.Form):
    delimiter = forms.ChoiceField(label="Choose delimiter", choices=DELIMITERS)
    file = forms.FileField()

class ChooseDataFormatForm(forms.Form):
    outputs = forms.MultipleChoiceField(label="Select output fields", required=True, widget=forms.CheckboxSelectMultiple)

    def set_choices(self, choices):
        self.fields["outputs"].choices = choices

class HiddenLayersForm(forms.Form):
    hidden_layers = forms.IntegerField(label="Number of hidden layers:", min_value=1)

class HiddenLayerForm(forms.Form):
    neurons = forms.IntegerField(label="Number of neurons", min_value=1, initial=1)
    activation = forms.ChoiceField(label="Activation function", choices=ACTIVATION_CHOICES)
    
class CompileFitForm(forms.Form):
    optimizer = forms.ChoiceField(label="Optimizer", choices=OPTIMIZERS)
    loss = forms.ChoiceField(label="Loss", choices=LOSSES)
    epochs = forms.IntegerField(label="Epochs", min_value=1)
    batch_size = forms.IntegerField(label="Batch size", min_value=1)
    