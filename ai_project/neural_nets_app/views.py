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
    hidden_layers = forms.IntegerField(label="Number of hidden layers", min_value=1)

class HiddenLayerForm(forms.Form):
    neurons = forms.IntegerField(label="Number of neurons", min_value=1, initial=1)
    activation = forms.ChoiceField(label="Activation function", choices=ACTIVATION_CHOICES)

# Create your views here.
def script(request):
    layers_form = HiddenLayersForm()
    layer_formset = formset_factory(HiddenLayerForm)
    
    if request.method == 'POST':
        if "layers_form" in request.POST:
            layers_form = HiddenLayersForm(request.POST)
        
            if layers_form.is_valid():
                layers_num = layers_form.cleaned_data["hidden_layers"]
                layer_formset = formset_factory(HiddenLayerForm, extra=layers_num)
        
        elif "layer_formset" in request.POST:
            formset = layer_formset(request.POST)
            
            if formset.is_valid():
                layers = []
                for form in formset:
                    layers.append(
                        {
                            "neurons": form.cleaned_data["neurons"],
                            "activation": form.cleaned_data["activation"]
                        }
                    )
                nn_scripts.run_neural_network(layers)          
        
    context = {
        'layers_form': layers_form,
        'layer_formset': layer_formset
    }
    
    return render(request, "neural_nets_app/nn_training.html", context=context)

def home(request):
    return render(request, "neural_nets_app/home.html")

def theory(request):
    return render(request, "neural_nets_app/nn_theory.html")

def user_guide(request):
    return render(request, "neural_nets_app/user_guide.html")