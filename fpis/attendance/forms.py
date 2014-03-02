
from django import forms
from models import *



class RecordForm(forms.ModelForm):
	
    class Meta:
        model = Record	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)

