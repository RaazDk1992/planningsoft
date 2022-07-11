from dataclasses import fields
from pyexpat import model
from django.db import models
from .models import FY, Comittee, ComitteeMembers, Designation, Doc, Finalize, MajorSector, Tippani, Woda,YojanaDetails,ProjectType,TypeOfProject,Office
from django import forms
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget



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

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = [
            'designation',
            'designation_en',
            'is_active'
        ]
        labels  = {
        'designation':'पद', 
        'designation_en':'पद अङ्ग्रजीमा', 
        'is_active':'सक्रिय'
        }
        widgets = {
            'designation': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Fiscal Year in English '
            }),
            'designation_en': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Fiscal Year in Nepali '
            }),
        }
class WodaForm(forms.ModelForm):
    class Meta:
        model = Woda
        fields = [
            'woda',
            'is_active'
        ]
        labels  = {
        'woda':'वडा नं', 
       
        'is_active':'सक्रिय'
        }
        widgets = {
            'woda': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'वडा नं'
            }),
        }
class MajorSectorsForm(forms.ModelForm):
    class Meta:
        model = MajorSector
        fields = [
            'section',
            'section_en',
            'is_active'
        ]
        labels  = {
        'section':'क्षेत्र', 
        'section_en': 'क्षेत्र अङ्ग्रेजीमा',
        'is_active':'सक्रिय'
        }
        widgets = {
            'section': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'क्षेत्र'
            }),
            'section_en': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'क्षेत्र'
            }),
        }


class CommitteeForm(forms.ModelForm):
     class Meta:
        model = Comittee
        fields = [
            'project_ref',
            'comittee_name',
            'comittee_name_en',
            'comittee_address',
            
        ]
        labels  = {
        'project_ref': 'आयोजना संकेत',
        'comittee_name':' समिति/ निर्माण ब्यवसायीको नाम ', 
        'comittee_name_en':'समिति/ निर्माण ब्यवसायीको नाम अङ्ग्रेजीमा', 
        'comittee_address':'ठेगाना'
        }
        widgets = {
             'project_ref': forms.HiddenInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':''
            }),
            'comittee_name': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':''
            }),
            'comittee_name_en': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':' '
            }),
            'comittee_address': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Fiscal Year in Nepali '
            }),
            
        }



class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = [
            'officeName',
            'officeAddress'
        ]
        labels  = {
        'officeName':'कार्यालयको नाम ', 
        'officeAddress':'ठेगाना '
       
        }
        widgets = {
            'officeName': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'कार्यालयको नाम '
            }),
            'officeAddress': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'ठेगाना'
            }),
        }
class DocForm(forms.ModelForm):
     class Meta:
        model = Doc
        fields = [
            'doc_name',
            'doc_body',
            'is_active'
        ]
        labels  = {
        'doc_name':' नाम ', 
        'doc_body':'ब्यहोरा ',
        'is_active':'सक्रिय'
       
        }
        widgets = {
            'doc_name': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'शिर्षक '
            }),
            'doc_body': SummernoteWidget(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'शिर्षक ',
            }),
        }

class ProjectTypesForms(forms.ModelForm):
    class Meta:
        model = ProjectType
        fields = [
            'sector_ref',
            'type',
            'type_en',
            'isActive'
        ]
        labels  = {
        'sector_ref':'क्षेत्र',
        'type':'आयोजनाकोरु प्रकार', 
        'type_en':'आयोजनाको प्रकार अङ्ग्रेजीमा', 
        'isActive':'सक्रिय'
        }
        widgets = {
            'sector_ref':forms.Select(attrs={'class':'form-control col-sm-6'}),
            'type': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'योजना प्रकार '
            }),
            'type_en': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Project Category in english '
            }),
        }
 
class TypeOfProjectForm(forms.ModelForm):
    class Meta:
        model = TypeOfProject
        fields = [
            'type_description',
            'type_description_en',
            'isActive'
        ]
        labels  = {
        'type_description':'आयोजनाकोरु प्रकृति', 
        'type_description_en':'आयोजनाको प्रकृति अङ्ग्रेजीमा', 
        'isActive':'सक्रिय'
        }
        widgets = {
            'type_description': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'योजना प्रकार '
            }),
            'type_description_en': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Project Category in english '
            }),
        }
 

class YojanaRegForm(forms.ModelForm):
    class Meta:
        model = YojanaDetails
        fields = [
             'fy_ref',
             'prj_ref',
             'prj_name' ,
             'area_ref',
             'prj_tole',
             'sector_ref',
             'prj_type',
             'type_prj_ref',
             'prj_start_date',
             'prj_start_date_en',
             'prj_completion_date',
             'prj_completion_date_en',
             'affected_people',
             'prj_estimate',
             'estimate_in_letters', 
             'is_multiyear',
             'is_active' ,
        ]
        labels  = {
             'fy_ref': 'आ.व',
             'prj_ref': 'योजना कोड',
             'prj_name': 'योजनाको नाम' ,
             'area_ref':'वडा नं',
             'prj_tole': 'योजना संचालन हुने स्थान',
             'sector_ref':'क्षेत्र',
             'prj_type':'योजनाको प्रकार',
             'type_prj_ref':'योजनाको प्रकृति',
             'prj_start_date':'योजना सुरु हुने मिति',
             'prj_completion_date':'योजना सम्पन्न हुने मिति',
             'affected_people': 'लाभान्वित जनसंख्या',
             'prj_estimate' : 'लागत ', 
             'estimate_in_letters': 'अक्षेरुपी रु.',
             'is_multiyear':  'बहुवर्षिय',
             'is_active': 'सक्रिय' ,
        }

        widgets = {
            'fy_ref':forms.Select(attrs={'class':'form-control col-sm-6'}),
            'prj_ref':forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Project code'
            }),
             'prj_name':forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':' योजनाको नाम'
            }),
            'area_ref':forms.Select(attrs={'class':'form-control col-sm-6'}),
             'prj_tole':forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'संचालन हुने स्थान'
            }),
            'sector_ref':forms.Select(attrs={'class':'form-control col-sm-6'}),
            'prj_type':forms.Select(attrs={'class':'form-control col-sm-6'}),
            'type_prj_ref': forms.Select(attrs={'class':'form-control col-sm-6'}),
            'prj_start_date': forms.TextInput(attrs={
                'class':'form-control col-sm-6 picker',
                'placeholder':'मिति छान्नुहोस्',
                'id':'prj_start'
            }),
             'prj_start_date_en': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'लाभान्वित जनसंख्या',
                'id':'prj_start_en'
            }),
             'prj_completion_date': forms.TextInput(attrs={
                'class':'form-control col-sm-6 picker',
                'placeholder':'मिति छान्नुहोस्',
                'id':'prj_complete'
            }),
            'prj_completion_date_en': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'id':'prj_complete_en'
            }),
            'affected_people': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'लाभान्वित जनसंख्या'
            }),
            'prj_estimate': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'लागत रु ',
                'id':'amt_number'
            }),
            'estimate_in_letters': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'लागत रु ',
                'id':'amt_ltrs'
            }),
        }
class MembersForm(forms.ModelForm):
    class Meta:
        model = ComitteeMembers
        fields = [
            'comittee_ref',
            'project_ref',
            'member_name',
            'member_designation',
            'member_citizen',
            'member_citizen_img',
            'member_image',
            'member_phone'
        ]
        labels  = {
            'member_name': 'नाम',
            'member_designation' : 'पद',
            'member_citizen':'नागरिकता नं',
            'member_citizen_img':'नागरिकता',
            'member_image':'फोटो',
            'member_phone':'फोन नं'
        }
        widgets = {
            'comittee_ref':forms.HiddenInput(attrs={'class':'form-control col-sm-6'}),
            'project_ref':forms.HiddenInput(attrs={'class':'form-control col-sm-6'}),
            'member_name': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'नाम '
            }),
            'member_designation':forms.Select(attrs={'class':'form-control col-sm-6'}) ,
            'member_citizen': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Project Category in english '
            }),
            'member_phone': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Mobile No. '
            }),
           
        }
class TippaniForm(forms.ModelForm):
     class Meta:
        model = Tippani
        fields = [
            'title',
            'file_path'
        ]
        labels  = {
        'title':'कागजातको नाम', 
        'file_path':'FilePath'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'कागजातको नाम '
            }),
            'fy_np': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Fiscal Year in Nepali '
            }),
        }
class FinalizeForm(forms.ModelForm):
    class Meta:
        model = Finalize
        fields = [
            'prj_ref',
            'to_date',
            'message'
        ]
        labels  = {
        'prj_ref':'योजना संकेत', 
        'to_date':'सम्झौताको लागि मिति तोक्नुहोस्',
        'message':'Message'
        }
        widgets = {
            'prj_ref': forms.TextInput(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'सम्झौताको लागि मिति तोक्नुहोस्'
            }),
            'to_date': forms.TextInput(attrs={
                'class':'form-control col-sm-6 picker',
                'placeholder':'मिति छान्नुहोस् ',
                'id':'date_picker_final'

            }),
            'message': forms.Textarea(attrs={
                'class':'form-control col-sm-6',
                'placeholder':'Type Message here.. ',
                'id':'base_text'
            }),
        }