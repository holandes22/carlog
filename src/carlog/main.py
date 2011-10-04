from django.shortcuts import render_to_response
from django.template.context import RequestContext

def carlog_main(request):
    return render_to_response('base.html', context_instance = RequestContext(request))
