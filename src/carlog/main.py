from django.shortcuts import render_to_response
from django.template import RequestContext as RequestContextTemplate
from django.template.context import RequestContext

from socialregistration.contrib.facebook.models import FacebookProfile

def carlog_main(request):
    return render_to_response('base.html', context_instance = RequestContext(request))

def search_page(request):
    return render_to_response('search/search.html', context_instance = RequestContext(request))

def auth_page(request):
    return render_to_response('registration/auth.html', {'facebook' : FacebookProfile.objects.all()},
                               context_instance = RequestContextTemplate(request))
 
    
    