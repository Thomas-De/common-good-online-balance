# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import CreateView, DetailView, UpdateView, ListView

from ecg_balancing.models import *


class CompanyListView(ListView):
    model = Company


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User


class CompanyDetailView(DetailView):
    model = Company


class CompanyUpdateView(UpdateView):
    model = Company


class CompanyBalanceDetailView(DetailView):
    model = CompanyBalance
    template_name = 'ecg_balancing/company_balance_detail.html'


class CompanyBalanceCreateView(CreateView):
    model = CompanyBalance


class CompanyBalanceUpdateView(UpdateView):
    model = CompanyBalance


class CompanyBalanceIndicatorDetailView(DetailView):
    model = CompanyBalanceIndicator
    template_name = 'ecg_balancing/company_balance_indicator_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyBalanceIndicatorDetailView, self).get_context_data(**kwargs)
        # TODO: simplify the query?
        subindicators = Indicator.objects.filter(parent=self.object.indicator).all().order_by('subindicator_number').all()
        context['subindicators'] = subindicators
        return context


class CompanyBalanceIndicatorCreateView(CreateView):
    model = CompanyBalanceIndicator


class CompanyBalanceIndicatorUpdateView(UpdateView):
    model = CompanyBalanceIndicator

