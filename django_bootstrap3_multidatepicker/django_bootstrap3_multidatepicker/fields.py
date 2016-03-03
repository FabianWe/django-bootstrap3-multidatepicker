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

from django.forms import fields
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _, ungettext_lazy

import json
import datetime

from .widgets import BootstrapDatepickerInput

class DateListField(fields.CharField):

    widget = BootstrapDatepickerInput

    default_error_messages = {
        'invalid': _('Enter a list of dates.'),
    }

    def __init__(self, max_length=1024, min_length=None, strip=True, *args, **kwargs):
        super(DateListField, self).__init__(max_length, min_length, strip, *args, **kwargs)

    def to_python(self, value):
        if isinstance(value, list):
            new_list = []
            for v in value:
                if isinstance(v, datetime.datetime):
                    new_list.append(v.date())
                elif isinstance(v, datetime.date):
                    new_list.append(v)
            return new_list
        if isinstance(value, datetime.datetime):
            return value.date()
        if isinstance(value, datetime.date):
            return value
        if value in self.empty_values:
            return None
        value = super(DateListField, self).to_python(value)
        dates = ''
        try:
            dates = json.loads(value)
            if type(dates) != list:
                raise ValidationError(self.error_messages['invalid'], code='invalid')
            result = []
            for date in dates:
                if type(date) != str:
                    raise ValidationError(self.error_messages['invalid'], code='invalid')
                m, y, d = None, None, None
                split = date.split('/')
                y, m, d = split
                y, m, d = int(y), int(m), int(d)
                result.append(datetime.date(y, m, d))
        except (ValueError, TypeError, json.JSONDecodeError):
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return result
