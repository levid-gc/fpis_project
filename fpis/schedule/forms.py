# -*- coding: utf-8 -*-

from django import forms
from .models import Term, Course
import datetime


def get_current_term_name():
    now = datetime.date.today()
    year = now.year

    if now.month <= 7:
        return str(year) + '年上半学期'
    else:
        return str(year) + '年下半学期'


class CreateTermForm(forms.Form):
    name = forms.CharField(label='名称',  max_length=50, required=True, error_messages={'required': '请输入学期或假期名称'})
    date_start = forms.DateField(label='开始日期', required=True, error_messages={'required': '开始日期不可为空'})
    date_end = forms.DateField(label='结束日期', required=True, error_messages={'required': '结束日期不可为空'})
    term_type = forms.BooleanField(label='是否为假期')

    def clean(self):
        """ Achieve all the original cleaned data """
        cleaded_data = super(CreateTermForm, self).clean()
        date_start = cleaded_data.get('date_start')
        date_end = cleaded_data.get('date_end')
        term_type = cleaded_data.get('term_type')

        if date_start and date_end:
            if date_end <= date_start:
                """ First step: validate the date """
                self._errors['date_end'] = self.error_class([u'结束日期必须大于开始日期'])
                del cleaded_data['date_end']
                return cleaded_data
            else:
                """ Second step: validate the weeks """
                delta = date_end - date_start
                if term_type:
                    """ The weeks between the start date and end date must in 3 to 9 """
                    if delta.days < 21:
                        self._errors['date_end'] = self.error_class([u'假期时间过短'])
                        del cleaded_data['date_end']
                        return cleaded_data
                    elif delta.days > 63:
                        self._errors['date_end'] = self.error_class([u'假期时间过长'])
                        del cleaded_data['date_end']
                        return cleaded_data
                else:
                    """ The weeks between the start date and end date must in 16 to 25 """
                    if delta.days < 112:
                        self._errors['date_end'] = self.error_class([u'学期时间过短'])
                        del cleaded_data['date_end']
                        return cleaded_data
                    elif delta.days > 175:
                        self._errors['date_end'] = self.error_class([u'学期时间过长'])
                        del cleaded_data['date_end']
                        return cleaded_data

        date_start = cleaded_data.get('date_start')
        date_end = cleaded_data.get('date_end')
        if date_start and date_end:
            """ The third step: validate the data with database """
            pass









class TermForm(forms.ModelForm):
	
    class Meta:
        model = Term	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(TermForm, self).__init__(*args, **kwargs)



class CourseForm(forms.ModelForm):
	
    class Meta:
        model = Course	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

