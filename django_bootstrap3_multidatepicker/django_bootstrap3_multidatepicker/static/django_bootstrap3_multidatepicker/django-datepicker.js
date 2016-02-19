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

function jsonDateFormat(date) {
  // returns the date as a string formatted by
  // yyyy/mm/dd
  // this way we will parse the date in python
  return dateFormat(date, 'yyyy/mm/dd');
}

function update_picker_input(picker_id, input_id, sort) {
  if (typeof(sort)==='undefined') sort = true;
  // create a list of all dates in the format
  var dates = $(picker_id).datepicker('getDates');
  if (sort) {
    dates.sort(function(a,b) {
      return a - b;
    });
  }
  var jsonData = [];
  for (var i = 0; i < dates.length; i++) {
    jsonData.push(jsonDateFormat(dates[i]));
  }
  $(input_id).val(JSON.stringify(jsonData));
}

function bind_picker(picker_id, input_id) {
  // create the actual picker
  $(picker_id).datepicker();

  // create an event that updates the value of an input field when the
  // selection changes
  $(picker_id).on("changeDate", function() {
    // call our update_input function, this way later on you could specify
    // a different behaviour (just be sure to call update_input)
    update_input(picker_id, input_id);
  });
}
