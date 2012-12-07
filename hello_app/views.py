# Create your views here.
from django.shortcuts import render
from hello_app.forms import *
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST': # If the form has been submitted...
        
        form = FeedbackForm(request.POST) # A form bound to the POST data
        
        if form.is_valid(): # All validation rules pass
            
            

            return HttpResponseRedirect('/thanks/') # Redirect after POST
    
    else:
        form = FeedbackForm() # An unbound form

    return render(request, 'index.html', {
        'form': form,
    })

def thanks(request):
    return render(request, 'thanks.html', {} )
