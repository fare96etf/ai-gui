import io
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.forms import formset_factory
from formtools.wizard.views import SessionWizardView
from .nn_scripts import nn_scripts
import pandas as pd

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

class UploadCsvForm(forms.Form):
    file = forms.FileField(label="Upload csv", required=True)

class ChooseDataFormat(forms.Form):
    outputs = forms.MultipleChoiceField(label="Choose output fields", required=True, widget=forms.CheckboxSelectMultiple)

    def set_choices(self, choices):
        self.fields["outputs"].choices = choices

class HiddenLayersForm(forms.Form):
    hidden_layers = forms.IntegerField(label="Number of hidden layers", min_value=1)

class HiddenLayerForm(forms.Form):
    neurons = forms.IntegerField(label="Number of neurons", min_value=1, initial=1)
    activation = forms.ChoiceField(label="Activation function", choices=ACTIVATION_CHOICES)


# Create your views here.
def upload_csv(request):
    if request.method == 'POST':
        csv = request.FILES['csv']
        csv_read = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            ),
            delimiter=","
        )
                
        global csv_data
        def csv_data():
            return csv_read
        
        return HttpResponseRedirect('step2')

    return render(request, "neural_nets_app/steps/1_upload_csv.html") 

def choose_data_format(request):
    choices = [(index, col) for index, col in enumerate(csv_data().columns.tolist())]
    
    if request.method == 'POST':
        print(request.POST)
        form = ChooseDataFormat(request.POST)
        form.set_choices(choices)
        
        if form.is_valid():    
            outputs = form.cleaned_data["outputs"]
            global output_cols
            def output_cols():
                return outputs
                    
            return HttpResponseRedirect('step3')
    else: 
        form = ChooseDataFormat()
        form.set_choices(choices)
    
    return render(request, "neural_nets_app/steps/2_choose_data_format.html", {"form": form}) 

def script(request):
    outputs = list(map(int, output_cols()))
    data = csv_data().values
    
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
                nn_scripts.run_neural_network(data, layers, outputs)          
        
    context = {
        'layers_form': layers_form,
        'layer_formset': layer_formset
    }
    
    return render(request, "neural_nets_app/steps/3_hidden_layers.html", context=context)

def home(request):
    return render(request, "neural_nets_app/home.html")

def theory(request):
    return render(request, "neural_nets_app/nn_theory.html")

def user_guide(request):
    return render(request, "neural_nets_app/user_guide.html")