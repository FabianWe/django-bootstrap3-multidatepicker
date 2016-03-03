/*!
Copyright 2016 Fabian Wenzelmann

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/


function DjangoBootstrapDatePicker(picker_id, input_id) {
  // a class that stores the picker_id and input_id
  this.picker_id = picker_id;
  this.input_id = input_id;
  this.dates = [];
}

DjangoBootstrapDatePicker.prototype.jsonDateFormat = function(date) {
  // returns the date as a string formatted by
  // yyyy/mm/dd
  // this way we will parse the date in python
  return dateFormat(date, 'yyyy/mm/dd');
};

DjangoBootstrapDatePicker.prototype.bind_picker = function(options) {
  // create the actual picker
  $(this.picker_id).datepicker(options);
  // if the field already contains some text
  // set the dates
  this.set_dates();
  // create an event that updates the value of an input field when the
  // selection changes
  $(this.picker_id).on("changeDate", call_me(this));
};

DjangoBootstrapDatePicker.prototype.set_dates = function(str) {
  if (typeof(str)==='undefined') {
    str = $(this.input_id).val();
    str = str.trim();
    if (!str) {
      return;
    }
  }
  var dates = [];
  var date_strs = JSON.parse(str);
  for (var i = 0; i < date_strs.length; i++) {
    var date_parts = date_strs[i].split('/');
    var year = parseInt(date_parts[0]);
    var month = parseInt(date_parts[1]) - 1;
    var day = parseInt(date_parts[2]);
    var date = new Date(year, month, day);
    dates.push(date);
  }
  $(this.picker_id).datepicker('setDates', dates);
};

function call_me(picker) {
  return function() {
    picker.on_change();
  };
}

DjangoBootstrapDatePicker.prototype.on_change = function() {
  // call our update_input function, this way later on you could specify
  // a different behaviour (just be sure to call update_input)
  this.update_picker_input(true);
}

DjangoBootstrapDatePicker.prototype.update_picker_input = function(sort) {
  if (typeof(sort)==='undefined') {
    sort = true;
  }
  // create a list of all dates in the format
  var dates = $(this.picker_id).datepicker('getDates');

  if (sort) {
    dates.sort(function(a,b) {
      return a - b;
    });
  }
  var jsonData = [];
  for (var i = 0; i < dates.length; i++) {
    jsonData.push(this.jsonDateFormat(dates[i]));
  }
  var resultStr = JSON.stringify(jsonData);
  this.dates = dates;
  $(this.input_id).val(resultStr);
  return true;
};
