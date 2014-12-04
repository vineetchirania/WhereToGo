from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponse
from forms import *

from recommend import find_destination

# Create your views here.
def recommend(request):
    return HttpResponse("Coming soon baby!")

def select_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            activities = form.cleaned_data.get('Activities')
            destinations = find_destination(activities)
            return render_to_response('show_cities.html',{'activities':activities,'city_list':destinations})
    else:
        form = ActivityForm

    return render_to_response('select_activity.html', {'form':form }, context_instance=RequestContext(request)) 
