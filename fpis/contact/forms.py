from django import forms
from django.forms import ModelForm
from contact.models import Suggestion


class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        exclude = ('approved',)


class FeedbackForm(forms.Form):
    email = forms.EmailField(label='Your Email')
    name = forms.CharField(label='Name')
    message = forms.CharField(label='Body', widget=forms.Textarea)
