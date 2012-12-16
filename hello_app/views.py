# Create your views here.
from django.shortcuts import render
from hello_app.forms import *
from django.http import HttpResponseRedirect
from hello_app.models import *

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        
        form = FeedbackForm(request.POST) # A form bound to the POST data
        
        if form.is_valid(): # All validation rules pass
            
            f = Feedback()

            f.name = form.cleaned_data['name']
            f.email = form.cleaned_data['email']
            f.wantsServicesXchange = form.cleaned_data['wantsServicesXchange']
            f.wantsGoodsXchange = form.cleaned_data['wantsGoodsXchange']
            f.wantsCharityXchange = form.cleaned_data['wantsCharityXchange']
            f.wantsLocationXchange = form.cleaned_data['wantsLocationXchange']
            f.wantsBadges = form.cleaned_data['wantsBadges']
            f.comments = form.cleaned_data['comments']

            f.save()

            return HttpResponseRedirect('/thanks/') # Redirect after POST

        #else: #if the form is NOT valid:

    
    else:
        form = FeedbackForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })

def thanks(request):
    return render(request, 'thanks.html', {} )


def index(request):
    return render(request, 'index.html')
