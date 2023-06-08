import io
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import formset_factory
from .nn_scripts import nn_scripts
import pandas as pd
from .forms import ChooseDataFormatForm, HiddenLayersForm, HiddenLayerForm, CompileFitForm

# Create your views here.
def app(request):
    return render(request, "neural_nets_app/steps/0_app.html") 

# step 1
def upload_csv(request):
    if request.method == 'POST':
        csv = request.FILES['csv']
        csv_read = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            ),
            delimiter=","
        )
                
        global nn_csv_data
        def nn_csv_data():
            return csv_read
        
        return HttpResponseRedirect('step2')

    return render(request, "neural_nets_app/steps/1_upload_csv.html") 

# step 2
def choose_data_format(request):
    choices = [(index, col) for index, col in enumerate(nn_csv_data().columns.tolist())]
    
    if request.method == 'POST':
        form = ChooseDataFormatForm(request.POST)
        form.set_choices(choices)
        
        if form.is_valid():    
            outputs = form.cleaned_data["outputs"]
            global nn_output_cols
            def nn_output_cols():
                return outputs
                    
            return HttpResponseRedirect('step3')
    else: 
        form = ChooseDataFormatForm()
        form.set_choices(choices)
    
    return render(request, "neural_nets_app/steps/2_choose_data_format.html", {"form": form}) 

# step 3
def layers(request):    
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
                global nn_layers
                def nn_layers():
                    return layers
                
                return HttpResponseRedirect('step4')         
        
    context = {
        'layers_form': layers_form,
        'layer_formset': layer_formset
    }
    
    return render(request, "neural_nets_app/steps/3_hidden_layers.html", context=context)

# step 4 + run script
def script(request):
    outputs = list(map(int, nn_output_cols()))
    data = nn_csv_data().values
    
    if request.method == 'POST':
        form = CompileFitForm(request.POST)
        
        if form.is_valid():
            optimizer = form.cleaned_data["optimizer"]
            loss = form.cleaned_data["loss"]
            epochs = form.cleaned_data["epochs"]
            batch_size = form.cleaned_data["batch_size"]
            
            compile_params = {
                "optimizer": optimizer,
                "loss": loss
            }
            
            fit_params = {
                "epochs": epochs,
                "batch_size": batch_size
            }
                
            nn_scripts.run_neural_network(data, nn_layers(), outputs, compile_params, fit_params) 
    else: 
        form = CompileFitForm()

    return render(request, "neural_nets_app/steps/4_compile_fit_params.html", {"form": form})

def home(request):
    return render(request, "neural_nets_app/home.html")

def theory(request):
    return render(request, "neural_nets_app/theory.html")

def user_guide(request):
    return render(request, "neural_nets_app/user_guide.html")