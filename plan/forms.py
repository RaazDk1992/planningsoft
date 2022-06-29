from dataclasses import fields
from pyexpat import model
from django.db import models
from .models import FY,YojanaDetails
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
class YojanaRegForm(forms.ModelForm):
    class Meta:
        model = YojanaDetails
        fields = [
             'fy_ref',
             'prj_ref',
             'prj_name' ,
             'prj_tole',
             'prj_type',
             'type_prj_ref',
             'affected_people',
             'prj_duration',
             'prj_estimate', 
             'is_active' ,
        ]
        labels  = {
             'fy_ref': 'आ.व',
             'prj_ref': 'योजना कोड',
             'prj_name': 'योजनाको नाम' ,
             'prj_tole': 'योजना संचालन हुने स्थान',
             'prj_type':'योजनाको प्रकार',
             'type_prj_ref':'योजनाको प्रकृति',
             'affected_people': 'लाभान्वित जनसंख्या',
             'prj_duration':'संचालन हुने समय',
             'prj_estimate' : 'लागत ', 
             'is_active': 'सक्िरय' ,
        }

        widgets = {
            'prj_type':forms.Select(attrs={'class':'form-control col-sm-6'}),
            'prj_ref':forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Project code'
            }),
             'prj_name':forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':' योजनाको नाम'
            }),
             'prj_tole':forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'संचालन हुने स्थान'
            }),
            'prj_type':forms.Select(attrs={'class':'form-control col-sm-6'}),
            'type_prj_ref': forms.Select(attrs={'class':'form-control col-sm-6'}),
            'affected_people': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'लाभान्वित जनसंख्या'
            }),
            'affected_people': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'लाभान्वित जनसंख्या'
            }),
            'prj_duration': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'योजना संचालन हुने अवधि'
            }),
            'prj_estimate': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'लागत रु '
            }),
        }