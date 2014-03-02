from django.shortcuts import render, render_to_response
from django.template import RequestContext
from contact.forms import FeedbackForm, SuggestionForm


def suggestion(request):
    if request.method == 'POST':
        return render_to_response('contact/suggestion.html', {'message': message}, context_instance=RequestContext(request))
    else:
        return render_to_response('contact/suggestion.html', {'form': SuggestionForm}, context_instance=RequestContext(request))



def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if(form.is_valid()):
            print(request.POST['name'])
            print(request.POST['message'])
            message = 'Thank you for you feedback.'
        else:
            message = 'Sorry, something went wrong.'
        return render_to_response('contact/contact.html', {'success': message}, context_instance=RequestContext(request))
    else:
        return render_to_response('contact/contact.html', {'form': FeedbackForm()}, context_instance=RequestContext(request))



# Create your views here.
