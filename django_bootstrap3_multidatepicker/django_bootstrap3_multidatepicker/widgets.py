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

from django.forms.widgets import Widget, flatatt, HiddenInput
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape, format_html, html_safe
from django.utils import translation

class BootstrapDatepickerInput(HiddenInput):
    class Media:
        # This class is inspired by a similar class in
        # https://pypi.python.org/pypi/django-bootstrap3-datepicker/0.3.1
        class JsFiles(object):
            def __iter__(self):
                yield 'django_bootstrap3_multidatepicker/django-datepicker.min.js'
                yield 'django_bootstrap3_multidatepicker/bootstrap-datepicker.min.js'
                yield 'django_bootstrap3_multidatepicker/date.format.min.js'
                lang = translation.get_language()
                if lang:
                    lang = lang.lower()
                    #There is language name that length>2 *or* contains uppercase.
                    lang_map = {
                        'nl-be': 'nl-BE',
                        'pt-br': 'pt-BR',
                        'rs-latin': 'rs-latin',
                        'zh-cn': 'zh-CN',
                        'zh-tw': 'zh-TW',
                    }
                    if len(lang) > 2:
                        lang = lang_map.get(lang, 'en-us')
                    if lang not in ('en', 'en-us'):
                        yield 'django_bootstrap3_multidatepicker/datepicker_locales/bootstrap-datepicker.%s.min.js' % (lang)
        css = {
            'all': ['django_bootstrap3_multidatepicker/bootstrap-datepicker3.standalone.min.css']
        }
        js = JsFiles()

    def __init__(self, attrs=None, options=None, div_attrs=None, icon_attrs=None):
        if not icon_attrs:
            icon_attrs = {'class': 'glyphicon glyphicon-calendar'}
        if not div_attrs:
            div_attrs = {'class': 'input-group date-list'}
        super(BootstrapDatepickerInput, self).__init__(attrs)
        if 'class' not in self.attrs:
            self.attrs['class'] = 'form-control'
        self.div_attrs = div_attrs and div_attrs.copy() or {}
        self.icon_attrs = icon_attrs and icon_attrs.copy() or {}
        self.picker_id = self.div_attrs.get('id') or None
        if options == False:  # datetimepicker will not be initalized only when options is False
            self.options = False
        else:
            self.options = options and options.copy() or {}


    def render(self, name, value, attrs=None):
        return 'TOLL'
