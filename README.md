# django-bootstrap3-datepicker
Datepicker that supports the selection of multiple dates for Django, using Bootstrap Twitter.

The aim of this package is to provide widgets and form fields for Django that use
[bootstrap-datepicker](http://bootstrap-datepicker.readthedocs.org/en/latest/index.html).

There are some packages that already try to do this, however I've never found one with working
multidate support.
The package's homepage can be found [here](https://github.com/FabianWe/django-bootstrap3-multidatepicker) on GitHub.

I'll slightly follow the package as provide [here](https://github.com/nkunihiko/django-bootstrap3-datetimepicker).
This package supports single date selection, mine will cover multidate selection.
Because that's not so much change I'll actually copy a lot from this code base.

# Notice
This package does what I want for a specific purpose, if you have any suggestions contact me!
This package is still in an early beta.

# Credits
I've used some libraries and I wish to thank the people who wrote them!
* Of course the [Django](https://www.djangoproject.com/) developers
* [bootstrap3_datepicker](http://bootstrap-datepicker.readthedocs.org/en/latest/index.html)
* [JavaScript Date Format](http://blog.stevenlevithan.com/archives/date-time-format)

And all the people I've forgotten ;).

# License
Licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

# Example Usage
There is a small demo included in this package.
However make sure that `'django_bootstrap3_multidatepicker'` and `'bootstrap3'` are contained in your `'INSTALLED_APPS'`.

You should also change the bootstrap3 default behaviour and take care that `'javascript_in_head'` is set to `True`, i.e.
put in your *settings.py*:

```python
BOOTSTRAP3 = {
    'javascript_in_head': True,
}
```

There is a widget called `BootstrapDatepickerInput` and a form field `DateListField`.
They should be used together, otherwise I can't guarantee anything ;).

The `DateListField` stores the dates as python list of `datetime.date` objects.
The hidden input stores a json list containing all the selected dates in the form `"yyyy/mm/dd"`, e.g. `"2016/02/22"`.
It's method `to_python` gets the string from the hidden input, tries to parse them in the given format and returns the
list of all dates.

Here's a small example that displays a calendar and lets the user select the inputs.

```python
from django import forms

from django_bootstrap3_multidatepicker import widgets, fields

class MyForm(forms.Form):
    dates = fields.DateListField(widget=widgets.BootstrapDatepickerInput)
```

Adding a template etc. will give you a calendar like this:

Reference-style:
![alt text][doc/imgs/widget_example.png]
