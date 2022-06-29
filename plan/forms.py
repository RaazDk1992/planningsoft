from django.db import models
from .models import FY,Profile
from django import forms
from django.contrib.auth.models import User


class FYform(forms.ModelForm):
    class Meta:
        model = FY
        fields = [
            'fy',
            'fy_np',
            'isactive'
        ]
        labels  = {
        'fy':'आ व (अङ्ग्रेजीमा)', 
        'fy_np':'आ व', 
        'isActive':'सक्रिय'
        }
        widgets = {
            'fy': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Fiscal Year in English '
            }),
            'fy_np': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Fiscal Year in Nepali '
            }),
        }