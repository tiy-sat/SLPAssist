var $ = require("jquery");

var $enterEmail = ("[data-js='parEmail']");
var $confirmEmail = ("[data-js='confEmail']");
var $emailError = ("[data-js='errorMsg']");

var $expandAddStudent = $("[data-js='dashboard_expandAddStudent']");
var $dashboardInput = $("[data-js='dashboard_input']");
var $addStudentForm = $("[data-js='add_student_form']")
var $studentName = $("[data-js='student_name']");
var $caregiverName = $("[data-js='caregiver_name']");
var $caregiverEmail = $("[data-js='caregiver_email']");
var $score = $("[data-js='score']");
var $addStudent = $("[data-js='add_student_button']");

this.expandField = function(){
  $expandAddStudent.on("click",function(e){
    $dashboardInput.toggleClass("hide");
  });
}

this.ajaxPOST = function(){
  $.fn.serializeObject = function(){
      var o = {};
      var a = this.serializeArray();
      $.each(a, function() {
          if (o[this.name] !== undefined) {
              if (!o[this.name].push) {
                  o[this.name] = [o[this.name]];
              }
              o[this.name].push(this.value || '');
          } else {
              o[this.name] = this.value || '';
          }
      });
      return o;
  };

  $addStudentForm.on("submit", function(e){
    e.preventDefault();

  var newStudentData = $addStudentForm.serializeObject();

      $.ajax({
        method: "POST",
        url: "/students",
        data: newStudentData,
        dataType: json,
        success: function(response){
          console.log(response);
        }
      });
  })

}
