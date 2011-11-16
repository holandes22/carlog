from types import MethodType

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import auth

from carlog.entries.models import Car, CarForm
from carlog.entries.models import CarMechanic, CarMechanicForm
from carlog.entries.models import CarTreatmentEntry, CarTreatmentEntryForm


#=======================================================================================================================
# Test Methods
#=======================================================================================================================

def mobile_test(request):
    car_list = CarMechanic.objects.filter(user = request.user)
    return render_to_response('mobile_test.html', {'car_list': car_list, 'user': request.user},
                              context_instance = RequestContext(request))   
    
#=======================================================================================================================
# Generic Methods 
#=======================================================================================================================

def generic_entry_summary(request, entry_list, available_actions):
    return render_to_response('entry/entry_summary.html', 
                              {'user': request.user, 'entry_list': entry_list, 'available_actions':available_actions}, 
                              context_instance = RequestContext(request))
    
def generic_entry_details(request, entry, available_actions):
    return render_to_response('entry/entry_details.html',
                              {'entry': entry, 'user': request.user, 'available_actions':available_actions}, 
                              context_instance = RequestContext(request))
    
#=======================================================================================================================
# CarMechanic Methods
#=======================================================================================================================

@login_required()
def car_summary(request):
    car_list = Car.objects.filter(user = request.user)
    return generic_entry_summary(request, car_list, Car.get_add_action())

@login_required() 
def car_details(request, id):
    car = get_object_or_404(Car, id = id)
    return generic_entry_details(request, car, car.get_common_actions())

@login_required()  
def car_editor(request, id = None):
    try:
        car = Car.objects.get(pk = id)
    except ObjectDoesNotExist:
        car = None
    form = CarForm(request.POST or None, instance = car)
    
    #Save new/edited System
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse('saved')
    
    submit_url = car and car.get_absolute_editor_url() or Car.get_model_editor_url()
    return render_to_response('editor.html', { 'form':form, 'submit_url': submit_url }, 
                              context_instance = RequestContext(request))

#=======================================================================================================================
# Mechanic methods
#=======================================================================================================================

@login_required()
def mechanic_summary(request):
    mechanic_list = CarMechanic.objects.filter(user = request.user)
    return generic_entry_summary(request, mechanic_list, CarMechanic.get_add_action())

@login_required() 
def mechanic_details(request, id):
    mechanic = get_object_or_404(CarMechanic, id = id)
    return generic_entry_details(request, mechanic, mechanic.get_common_actions())
    
@login_required()  
def mechanic_editor(request, id = None):
    try:
        mechanic = CarMechanic.objects.get(pk = id)
    except ObjectDoesNotExist:
        mechanic = None
    form = CarMechanicForm(request.POST or None, instance = mechanic)
    
    #Save new/edited System
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse('saved')
    
    submit_url = mechanic and mechanic.get_absolute_editor_url() or CarMechanic.get_model_editor_url()
    return render_to_response('editor.html', { 'form':form, 'submit_url': submit_url }, 
                              context_instance = RequestContext(request))
    
#=======================================================================================================================
# Treatment methods 
#=======================================================================================================================

@login_required()
def treatment_summary(request, car_id):
    car = get_object_or_404(Car, id = car_id)
    treatment_list = CarTreatmentEntry.objects.filter(car = car)
    return render_to_response('treatment/treatment_summary.html', 
                              {
                               'user': request.user, 
                               'entry_list': treatment_list, 
                               'available_actions': CarTreatmentEntry.get_add_action(),
                               'grid_url': '/entries/treatment/car/%s/summary/get_grid/' % car.id,
                               }, 
                              context_instance = RequestContext(request))    

@login_required() 
def treatment_details(request, id):
    treatment = get_object_or_404(CarTreatmentEntry, id = id)
    return generic_entry_details(request, treatment, treatment.get_common_actions())

def get_car_treatment_data_as_xml_string(car_id):
    car = get_object_or_404(Car, id = car_id)
    treatment_list = CarTreatmentEntry.objects.filter(car = car)
    
    editor_button_html = """<cell><![CDATA[<button onclick="$('#editor_dialog').load('%s').dialog('open');">Edit</button>]]></cell>"""
    delete_button_html = """<cell><![CDATA[<button onclick="alert('Delete url is %s')">Delete</button>]]></cell>"""

    data = "<?xml version='1.0' encoding='utf-8'?>"
    data += "<rows>"
    data += "<page>%s</page>" % 1
    data += "<total>%d</total>" % (len(treatment_list) / 10)
    data += "<records>%d</records>" % len(treatment_list)
    for treatment in treatment_list:
        data += "<row id='%s'>" % treatment.id
        for key, value in treatment.get_model_attrs():
            if isinstance(value, MethodType):
                value = value()
            data += "<cell>%s</cell>" % value
        data += editor_button_html % treatment.get_absolute_editor_url()
        data += delete_button_html % treatment.get_delete_entry_url()
        data += "</row>"
    data += "</rows>"
    
    return data    

def get_treatment_grid(request, car_id):
    data = get_car_treatment_data_as_xml_string(car_id)
    return HttpResponse(data, content_type = "text/xml;charset=utf-8")

    
@login_required()  
def treatment_editor(request, id = None):
    try:
        treatment = CarTreatmentEntry.objects.get(pk = id)
    except ObjectDoesNotExist:
        treatment = None
    form = CarTreatmentEntryForm(request.POST or None, instance = treatment)
    
    #Save new/edited System
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse('saved')
    
    submit_url = treatment and treatment.get_absolute_editor_url() or CarTreatmentEntry.get_model_editor_url()
    return render_to_response('editor.html', { 'form':form, 'submit_url': submit_url }, 
                              context_instance = RequestContext(request))

