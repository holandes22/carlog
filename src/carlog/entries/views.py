from django.shortcuts import render_to_response
from django.template.context import RequestContext

from carlog.entries.models import Car
    
def car_index(request):
    return render_to_response('car/car_index.html', {'car_list': Car.objects.all()}, 
                              context_instance = RequestContext(request))