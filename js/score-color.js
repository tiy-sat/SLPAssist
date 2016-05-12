var $ = require("jquery");

$(function(){
 console.log("here is the student score code")
  $("[data-js='student_score']").each(function(){
    if (this.val() > 5){
      this.css("color", "$successGreen");
    }

  });
})
