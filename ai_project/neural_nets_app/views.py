from django.shortcuts import render
from django import forms
from django.forms import formset_factory
from .nn_scripts import nn_scripts

ACTIVATION_CHOICES = [
    ("relu", "relu"),
    ("sigmoid", "sigmoid"), 
    ("softmax", "softmax"), 
    ("softplus", "softplus"), 
    ("softsign", "softsign"), 
    ("tanh", "tanh"), 
    ("selu", "selu"), 
    ("elu", "elu"), 
    ("exponential", "exponential")
]

class HiddenLayersForm(forms.Form):
    layers_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    hidden_layers = forms.IntegerField(label="Number of hidden layers", min_value=1)

class HiddenLayerForm(forms.Form):
    layer_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    neurons = forms.IntegerField(label="Number of neurons", min_value=1)
    activation = forms.ChoiceField(label="Activation function", choices=ACTIVATION_CHOICES)

# Create your views here.
def index(request):
    layers_form = HiddenLayersForm()
    layer_formset = formset_factory(HiddenLayerForm)
    
    if request.method == 'POST':
        print(request.POST)
        if 'layers_form' in request.POST:
            layers_form = HiddenLayersForm(request.POST, request.FILES)
        
            if layers_form.is_valid():
                print("radi prva forma")
                layer_formset = formset_factory(HiddenLayerForm, extra=layers_form.cleaned_data["hidden_layers"])
        
        if 'form-0-layer_form' in request.POST:
            print("radi druga forma")
            formset = layer_formset(request.POST)
            print(formset)
        
            if formset.is_valid():
                for form in formset:
                    print(form)
        
    context = {
        'layers_form': layers_form,
        'layer_formset': layer_formset
    }
    
    return render(request, "neural_nets_app/index.html", context=context)