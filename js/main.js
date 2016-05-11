var $ = require("jquery");

var $expandAddStudent = $("[data-js='dashboard_expandAddStudent']");
var $dashboardInput = $("[data-js='dashboard_input']");

$(function(){
  // Code here!

  $expandAddStudent.on("click",function(e){
    $dashboardInput.toggleClass("hide");
  });

});
