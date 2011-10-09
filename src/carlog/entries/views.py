from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import auth


from carlog.entries.models import Car, CarTreatmentEntry
from carlog.entries.models import CarForm


def mobile_test(request):
    car_list = Car.objects.filter(user = request.user)
    return render_to_response('mobile_test.html', {'car_list': car_list, 'user': request.user},
                              context_instance = RequestContext(request))    

def generic_editor(request, type, id = None):
    object_name = type.capitalize()
    object_form_name = '%sForm' % object_name
    object = getattr(carlog.entries.models, object_name, None)
    object_form = getattr(carlog.entries.models, object_form_name, None)
    if not object_form or not object:
        return Http404
    
    
    form = object_form(request.POST or None, instance = id and object.objects.get(pk = id))
    submit_url = id and "/entries/%s/%s/editor/" % (type, id) or "/entries/%s/editor/" % (type)
    # Save new/edited System
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')
    
    return render_to_response('editor.html', { 'form':form, 'submit_url': submit_url }, 
                              context_instance = RequestContext(request))

@login_required()
def car_index(request):
    car_list = Car.objects.filter(user = request.user)
    return render_to_response('car/car_index.html', {'car_list': car_list, 'user': request.user}, 
                              context_instance = RequestContext(request))

@login_required()
def car_summary(request):
    car_list = Car.objects.filter(user = request.user)
    return render_to_response('car/car_summary.html', {'car_list': car_list, 'user': request.user}, 
                              context_instance = RequestContext(request))

@login_required() 
def car_details(request, id):
    car = get_object_or_404(Car, id = id)
    return render_to_response('car/car_details.html', {'car': car, 'user': request.user}, 
                              context_instance = RequestContext(request))
    
def car_editor(request, id = None):
    form = CarForm(request.POST or None, instance = id and Car.objects.get(pk = id))
    submit_url = id and "/entries/car/%s/editor/" % id or "/entries/car/editor/"
    # Save new/edited System
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')
    
    return render_to_response('editor.html', { 'form':form, 'submit_url': submit_url }, 
                              context_instance = RequestContext(request))


@login_required()
def treatment_index(request, id):
    car = get_object_or_404(Car, id = id)
    treatment_list = CarTreatmentEntry.objects.filter(car = car)
    if len(treatment_list) == 0:
        return render_to_response('no_entries.html')
    filters = 'Car %s' % (car,) 
    return render_to_response('treatment/treatment_index.html', {'treatment_list': treatment_list, 'filters': filters}, 
                              context_instance = RequestContext(request))
    

