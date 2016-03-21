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
from django.utils.html import conditional_escape, format_html, html_safe, escape
from django.utils import translation
from django.utils.encoding import force_text

import json

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
                        'ar-ma': 'ar-ma',
                        'en-au': 'en-au',
                        'en-ca': 'en-ca',
                        'en-gb': 'en-gb',
                        'en-us': 'en-us',
                        'fa-ir': 'fa-ir',
                        'fr-ca': 'fr-ca',
                        'ms-my': 'ms-my',
                        'pt-br': 'bt-BR',
                        'rs-latin': 'rs-latin',
                        'tzm-la': 'tzm-la',
                        'tzm': 'tzm',
                        'zh-cn': 'zh-CN',
                        'zh-tw': 'zh-TW',
                        'zh-hk': 'zh-TW',
                    }
                    if len(lang) > 2:
                        lang = lang_map.get(lang, 'en-us')
                    if lang not in ('en', 'en-us'):
                        yield 'django_bootstrap3_multidatepicker/datepicker_locales/bootstrap-datepicker.%s.min.js' % (lang)
        css = {
            'all': ['django_bootstrap3_multidatepicker/bootstrap-datepicker3.standalone.min.css']
        }
        js = JsFiles()

    def __init__(self, attrs=None, options=None, div_attrs=None, icon_attrs=None, js_var=None):
        if not icon_attrs:
            icon_attrs = {'class': 'glyphicon glyphicon-calendar'}
        if not div_attrs:
            div_attrs = {'class': 'input-group date-list'}
        self.js_var = js_var
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
            self.options['multidate'] = True

    def input_tags(self):
        return '<input{input_attrs}>', '</input>'

    def input_content(self):
        return ''

    def input(self):
        input_open, input_close = self.input_tags()
        return input_open + self.input_content() + input_close

    def div_tags(self):
        return '<div{div_attrs}>', '</div>'

    def div_content(self):
        res = '''
        <span class="input-group-addon">
            <span{icon_attrs}></span>
        </span>
            '''
        return res

    def div(self):
        div_open, div_close = self.div_tags()
        return div_open + self.div_content() + div_close


    def js_tags(self):
        return '<script type="text/javascript">', '</script>'

    def js_content(self):
        res = '''
        $(document).ready(function() {{
            var {var_name} = new DjangoBootstrapDatePicker("#{picker_id}", "#{input_id}");
            {var_name}.bind_picker({options});
        }});
        '''
        return res

    def js(self):
        js_open, js_close = self.js_tags()
        return js_open + self.js_content() + js_close


    def render(self, name, value, attrs=None):
        print(value)
        input_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        icon_attrs = dict([(key, conditional_escape(val)) for key, val in self.icon_attrs.items()])
        if not self.picker_id:
            self.picker_id = (input_attrs.get('id', '') +
                               '_pickers').replace(' ', '_')
        self.div_attrs['id'] = self.picker_id
        if not self.js_var:
            self.js_var = (input_attrs.get('id', '') + '_jsvar').replace(' ', '_')
            self.js_var = self.js_var.replace('-', '_')
        div = self.div()
        div = format_html(div, div_attrs=flatatt(self.div_attrs), icon_attrs=flatatt(icon_attrs))
        input_ = self.input()
        input_ = format_html(input_, input_attrs=flatatt(input_attrs))
        js = self.js()
        # hopefully this is correct...
        js = js.format(var_name=self.js_var, picker_id=self.picker_id, input_id=input_attrs['id'], options=json.dumps(self.options))
        content = div + '\n' + input_ + '\n' + js
        return mark_safe(force_text(content))
