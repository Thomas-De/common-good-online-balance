# -*- coding: utf-8 -*-
from crispy_forms.layout import Layout, HTML

from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from ecg_balancing.models import UserProfile, Company, Indicator, CompanyBalance


class IndicatorForm(forms.ModelForm):

    class Meta:
        model = Indicator


class UserProfileForm(forms.ModelForm):
    helper = FormHelper()
    helper.label_class = 'clearboth text-right col-lg-2 col-md-2'
    helper.field_class = 'col-lg-5 col-md-5'
    helper.form_tag = False

    class Meta:
        model = UserProfile
        #fields = ('user.first_name', 'user.last_name', 'user.email')
        #exclude = ['creation_date']


class CompanyForm(forms.ModelForm):
    helper = FormHelper()
    helper.label_class = 'clearboth text-right col-lg-2 col-md-2'
    helper.field_class = 'col-lg-5 col-md-5'
    helper.form_tag = False

    class Meta:
        model = Company
        #fields = ('user.first_name', 'user.last_name', 'user.email')
        exclude = ['model_creation_date']


class CompanyBalanceForm(forms.ModelForm):
    helper = FormHelper()
    helper.label_class = 'clearboth text-right col-lg-2 col-md-2'
    helper.field_class = 'col-lg-5 col-md-5'
    helper.form_tag = False

    class Meta:
        model = CompanyBalance
        fields = ('matrix', 'year', 'company')

    def __init__(self, *args, **kwargs):
        super(CompanyBalanceForm, self).__init__(*args, **kwargs)
        self.fields['company'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super(CompanyBalanceForm, self).clean()
        year = cleaned_data.get("year")
        company = cleaned_data.get("company")

        existing_balance = CompanyBalance.objects.filter(company=company, year=year)
        if existing_balance.exists():
            raise forms.ValidationError(_('There is an existing balance for the year %s. Please enter another year.'%year))

        return cleaned_data
