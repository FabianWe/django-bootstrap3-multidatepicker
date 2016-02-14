# views.py

# Copyright (C) 2016 Fabian Wenzelmann
#
# This file is part of django-bootstrap3-datepicker.
#
# django-bootstrap3-datepicke is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-bootstrap3-datepicker is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-bootstrap3-datepicker.
# If not, see <http://www.gnu.org/licenses/>.
#

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import FormView

from bootstrap_datepicker_demo import forms

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ContactView(FormView):
    form_class = forms.DemoForm
    template_name = 'bootstrap_datepicker_demo/demo.html'
    def form_valid(self, form):
        return HttpResponse("DONE.")
