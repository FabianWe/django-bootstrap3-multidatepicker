# Copyright 2016 Fabian Wenzelmann

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView

from .forms import *

# Create your views here.

class MultiDateForm(FormView):
    template_name = 'multidate_demo/multi_date.html'
    form_class = ContactForm

    def form_valid(self, form):
        dates = form.cleaned_data['dates']
        return render(self.request, 'multidate_demo/multidate_success.html', {'dates': dates})
