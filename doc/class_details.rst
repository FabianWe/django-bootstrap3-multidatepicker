Class documentation
*******************

.. module:: django_bootstrap3_multidatepicker.django_bootstrap3_multidatepicker.fields

DateListField
=============

.. class:: DateListField(fields.CharField)

  The class ``DateListField`` provides a django form field for storing dates,
  it actually is a sublcass of (:class:`django:django.forms.fields.CharField`).

  You can use the same arguments as for a
  :class:`django:django.forms.fields.CharField`, for example ``max_length`` or
  ``min_length``. Note that this is the length of the text field that is
  used to store a JSON list representation of the selected dates, NOT the number
  of dates. The JSON representation is given in the format ``"yyyy/mm/dd"``,
  the JSON string may also contain ``"["``, ``"]"``, ``","`` etc.
  So you should set ``max_length`` to something reasonable by yourself.

  You can also use ``required=True`` as for a "normal" ``CharField``, this means
  that at least one date must be selected.

  .. method:: DateListField.to_python(value)

    Translates the string representation (value) to a list of dates

    :param str value: The string to translate
    :raises ValidationError: If value isn't a valid JSON string

    .. note::
      Usually you don't have to call this method yourself - django will take
      care of it if you use this field in a form.

    This method will call the ``to_python`` method of ``CharField`` in order to
    perform the validation checks there (like length validation).
    It further tries to parse the input as JSON. If the input isn't valid JSON
    it raises a ``ValidationError``. The JSON must contain a list of strings
    in the right format, i.e. ``"yyyy/mm/dd"`` with valid values for year,
    month and day (as described in :class:`datetime.date`). If this isn't the
    case, the method raises a ``ValidationError``.

    .. note::
      The months in javascript are zero based, so January is represented by
      ``"00"``. This method always adds one to the month because the python
      constructor uses values 1 <= month <= 12.
