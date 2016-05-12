var $ = require("jquery");

var $enterEmail = ("[data-js='parEmail']");
var $confirmEmail = ("[data-js='confEmail']");
var $emailError = ("[data-js='errorMsg']");

var $expandAddStudent = $("[data-js='dashboard_expandAddStudent']");
var $dashboardInput = $("[data-js='dashboard_input']");

this.expandField = function(){
  $expandAddStudent.on("click",function(e){
    $dashboardInput.toggleClass("hide");
  });
}

this.ajaxTest = function(){
  $.ajax({
    method: "POST",
    url: "/students",
    data: { stuName: "Johnny Boston", parName: "Poppa Boston", score: 3 },
    success: function(response){
      console.log(response);
    }
  });
}

  })
