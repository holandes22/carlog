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
# CarMechanic Methods
#=======================================================================================================================

@login_required()
def car_summary(request):
    car_list = Car.objects.filter(user = request.user)
    available_actions = [car_list[0].get_common_actions()[0]]
    return render_to_response('entry/entry_summary.html', 
                              {'entry_list': car_list, 'user': request.user,'available_actions':available_actions}, 
                              context_instance = RequestContext(request))

@login_required() 
def car_details(request, id):
    car = get_object_or_404(Car, id = id)
    available_actions = car.get_common_actions()
    return render_to_response('entry/entry_details.html',
                              {'entry': car, 'user': request.user, 'available_actions':available_actions}, 
                              context_instance = RequestContext(request))

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
    available_actions = [mechanic_list[0].get_common_actions()[0]]
    return render_to_response('entry/entry_summary.html', 
                              {'entry_list': mechanic_list, 'user': request.user,'available_actions':available_actions}, 
                              context_instance = RequestContext(request))

@login_required() 
def mechanic_details(request, id):
    mechanic = get_object_or_404(CarMechanic, id = id)
    available_actions = mechanic.get_common_actions()
    return render_to_response('entry/entry_details.html',
                              {'entry': mechanic, 'user': request.user, 'available_actions':available_actions}, 
                              context_instance = RequestContext(request))
    
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
def treatment_index(request, id):
    car = get_object_or_404(CarMechanic, id = id)
    treatment_list = CarTreatmentEntry.objects.filter(car = car)
    if len(treatment_list) == 0:
        return render_to_response('no_entries.html')
    filters = 'CarMechanic %s' % (car,) 
    return render_to_response('treatment/treatment_index.html', {'treatment_list': treatment_list, 'filters': filters}, 
                              context_instance = RequestContext(request))


@login_required()
def treatment_summary(request, car_id):
    car = get_object_or_404(Car, id = car_id)
    treatment_list = CarTreatmentEntry.objects.filter(car = car)
    available_actions = [treatment_list[0].get_common_actions()[0]]
    return render_to_response('entry/entry_summary.html', 
                              {'entry_list': treatment_list, 'user': request.user,'available_actions':available_actions}, 
                              context_instance = RequestContext(request))

@login_required() 
def treatment_details(request, id):
    treatment = get_object_or_404(CarTreatmentEntry, id = id)
    available_actions = treatment.get_common_actions()
    return render_to_response('entry/entry_details.html',
                              {'entry': treatment, 'user': request.user, 'available_actions':available_actions}, 
                              context_instance = RequestContext(request))
    
@login_required()  
def treatment_editor(request, id = None):
    try:
        treatment = CarTreatmentEntry.objects.get(pk = id)
    except ObjectDoesNotExist:
        mechanic = None
    form = CarTreatmentEntryForm(request.POST or None, instance = treatment)
    
    #Save new/edited System
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse('saved')
    
    submit_url = mechanic and mechanic.get_absolute_editor_url() or CarMechanic.get_model_editor_url()
    return render_to_response('editor.html', { 'form':form, 'submit_url': submit_url }, 
                              context_instance = RequestContext(request))

