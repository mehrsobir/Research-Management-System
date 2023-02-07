from django.core.exceptions import NON_FIELD_ERRORS

from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['year', 'topic', 'print_list']
        # model.year = forms.ModelChoiceField(queryset=,limit_choices_to=1)
        error_messages = {
            'year': {
                'max_length': "This writer's name is too long.",
            },
            NON_FIELD_ERRORS: {
                'unique_together': " are not unique.",
            },
        }

