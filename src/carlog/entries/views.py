from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from carlog.entries.models import Car, CarTreatmentEntry

def car_index(request):
    return render_to_response('car/car_index.html', {'car_list': Car.objects.all()}, 
                              context_instance = RequestContext(request))
    
def car_details(request, brand, car_id):
    car = get_object_or_404(Car, brand = brand, car_id = car_id)
    return render_to_response('car/car_details.html', {'car': car}, 
                              context_instance = RequestContext(request))
    
def treatment_index(request, brand, car_id):
    car = get_object_or_404(Car, brand = brand, car_id = car_id)
    treatment_list = CarTreatmentEntry.objects.filter(car = car)
    filters = 'Car %s' % (car,) 
    return render_to_response('treatment/treatment_index.html', {'treatment_list': treatment_list, 'filters': filters}, 
                              context_instance = RequestContext(request))